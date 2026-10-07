# cloudsim-day1
# CloudSim Network Datacenter Simulation — Cloud Computing Lab

## Overview
This lab experiment demonstrates how to simulate a **network-aware datacenter** using **CloudSim 3.0.3** in the **Eclipse IDE**. The experiment uses CloudSim's networking package to model edge switches, hosts, and network topology within a datacenter, then runs a cloudlet scheduling simulation on top of it.

## Objective
- Set up and run a CloudSim project in Eclipse.
- Understand how CloudSim models network datacenters using `EdgeSwitch`, `NetworkHost`, and `NetworkDatacenter` classes.
- Create a network topology by mapping hosts to edge switches.
- Execute cloudlets on the simulated datacenter and analyze the output.

## Tools Used
- Eclipse IDE
- CloudSim 3.0.3 framework
- Java (JDK — run via `javaw.exe`)

## Installation of CloudSim

1. **Install Java (JDK)**
   - Download and install a JDK (e.g. JDK 8 or above) from [Oracle](https://www.oracle.com/java/technologies/downloads/) or use OpenJDK.
   - Verify installation by running `java -version` in the command prompt/terminal.

2. **Install Eclipse IDE**
   - Download **Eclipse IDE for Java Developers** from [eclipse.org/downloads](https://www.eclipse.org/downloads/).
   - Extract/install and launch Eclipse, then select a workspace folder.

3. **Download CloudSim**
   - Go to the CloudSim GitHub repository: [https://github.com/Cloudslab/cloudsim](https://github.com/Cloudslab/cloudsim)
   - Download the CloudSim 3.0.3 release (ZIP) or clone the repository.
   - Extract the ZIP file to a known location on your system (e.g. `E:\DOWNLOAD\cloudsim-3.0.3`).

4. **Verify CloudSim JAR/Source**
   - Confirm the extracted folder contains the `source`, `examples`, and `jars` (or `modules`) folders — these will be imported into Eclipse.

## Creating a New CloudSim Project in Eclipse

1. Open Eclipse and go to **File → New → Java Project**.
2. Enter the project name (e.g. `cloudsim1`).
3. Uncheck **Use default location**, then click **Browse** and select the extracted `cloudsim-3.0.3` folder as the project location.
4. Click **Finish**. Eclipse imports the existing CloudSim source and example folders directly into the new project.
5. Expand the project tree in **Package Explorer** to confirm the packages (`org.cloudbus.cloudsim.examples`, `org.cloudbus.cloudsim.examples.network.datacenter`, etc.) are visible without red error markers.
6. If there are compilation errors, right-click the project → **Refresh**, then **Project → Clean...** to rebuild.

## Project Structure
```
cloudsim1
└── cloudsim-3.0.3/examples
    └── org.cloudbus.cloudsim.examples.network.datacenter
        ├── TestBagOfTaskApp.java
        └── TestExample.java
```

## Key Code — Network Creation
The core of this experiment is the `CreateNetwork` method, which builds the datacenter's network topology:

```java
static void CreateNetwork(int numhost, NetworkDatacenter dc) {

		// Edge Switch
		EdgeSwitch edgeswitch[] = new EdgeSwitch[1];

		for (int i = 0; i < 1; i++) {
			edgeswitch[i] = new EdgeSwitch("Edge" + i, NetworkConstants.EDGE_LEVEL, dc);
			// edgeswitch[i].uplinkswitches.add(null);
			dc.Switchlist.put(edgeswitch[i].getId(), edgeswitch[i]);
			// aggswitch[(int)
			// (i/Constants.AggSwitchPort)].downlinkswitches.add(edgeswitch[i]);
		}

		for (Host hs : dc.getHostList()) {
			NetworkHost hs1 = (NetworkHost) hs;
			hs1.bandwidth = NetworkConstants.BandWidthEdgeHost;
			int switchnum = (int) (hs.getId() / NetworkConstants.EdgeSwitchPort);
			edgeswitch[switchnum].hostlist.put(hs.getId(), hs1);
			dc.HostToSwitchid.put(hs.getId(), edgeswitch[switchnum].getId());
			hs1.sw = edgeswitch[switchnum];
			List<NetworkHost> hslist = hs1.sw.fintimelistHost.get(0D);
			if (hslist == null) {
				hslist = new ArrayList<NetworkHost>();
				hs1.sw.fintimelistHost.put(0D, hslist);
			}
			hslist.add(hs1);

		}

	}
```

This method:
1. Creates an `EdgeSwitch` to connect hosts within the datacenter.
2. Assigns each host in the datacenter to a switch based on its ID and the switch's port capacity.
3. Registers the host-to-switch mapping so the simulator can route network traffic correctly.

## Steps Followed
1. Imported the `cloudsim-3.0.3` project into Eclipse and added it to the `cloudsim1` workspace.
2. Navigated to `org.cloudbus.cloudsim.examples.network.datacenter` and opened `TestExample.java`.
3. Reviewed/wrote the `CreateNetwork` method to build the edge switch topology and map hosts to switches.
4. Ran `TestExample.java` as a Java Application from Eclipse.
5. Observed the simulation output in the **Console**, showing cloudlet execution results (Cloudlet ID, status, resource ID, VM ID, start time, finish time).

## Output
The console output shows each cloudlet's execution status:

```
Cloudlet ID   STATUS    Resource ID   VM ID   Time   Start Time   Finish Time
291           SUCCESS   2             5       801    19223        20024
294           SUCCESS   2             5       801    19223        20024
297           SUCCESS   2             5       801    19223        20024
278           SUCCESS   2             3       803    19268        20071
281           SUCCESS   2             3       803    19268        20071
...
numberofcloudlet 300  Cached 0  Data transfered 200000
CloudSimExample1 finished!
```

This confirms that all 300 cloudlets were **successfully executed** across the simulated network datacenter, with `200000` units of data transferred during the simulation.
<img width="1917" height="1002" alt="test example1" src="https://github.com/user-attachments/assets/a4d38ed1-9791-420b-a576-edac1ea6fc7c" />

## Learning Outcome
Through this experiment, I learned:
- How CloudSim models network topology inside a datacenter using switches (`EdgeSwitch`) and network-aware hosts (`NetworkHost`).
- How hosts are mapped to switches based on port capacity, simulating realistic network segmentation.
- How to run and interpret cloudlet scheduling results in a network-simulated CloudSim environment.
- The difference between a standard CloudSim datacenter and a **NetworkDatacenter**, which adds network latency/bandwidth modeling to the simulation.


