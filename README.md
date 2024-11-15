### Trade-offs for Each Approach

#### App-native Metrics

**Pros:**
- **Simplicity**: Directly integrates with the application, reducing the need for additional components.
- **Performance**: Lower latency as metrics are collected and exposed directly by the application.
- **Consistency**: Metrics are always in sync with the application's state.

**Cons:**
- **Coupling**: Tightly couples the metrics collection with the application logic, making it harder to maintain and test.
- **Scalability**: May require changes to the application code if the metrics collection needs to be updated or scaled.
- **Resource Usage**: Increases the resource usage of the application container, potentially affecting its performance.

#### Aggregator Sidecar

**Pros:**
- **Decoupling**: Separates metrics collection from the application logic, making it easier to maintain and test.
- **Flexibility**: Can be updated or scaled independently of the application.
- **Isolation**: Reduces the impact on the application's performance by offloading metrics collection to a separate container.

**Cons:**
- **Complexity**: Adds an additional component to the deployment, increasing the overall complexity.
- **Latency**: Potentially higher latency as metrics are collected from logs rather than directly from the application.
- **Synchronization**: Requires careful handling to ensure that the logs and metrics are in sync.