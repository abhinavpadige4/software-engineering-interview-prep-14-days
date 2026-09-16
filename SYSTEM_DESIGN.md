# System Design Preparation

## Overview
This document contains system design concepts, common questions, and resources for software engineering interview preparation.

## Key Concepts to Review

### 1. Scalability
- Vertical vs Horizontal scaling
- Load balancing algorithms (Round Robin, Least Connections, IP Hash)
- Caching strategies (CDN, Redis, Memcached)
- Database sharding and partitioning

### 2. Availability & Reliability
- Replication strategies (Master-Slave, Master-Master)
- Fault tolerance and redundancy
- Circuit breaker pattern
- Health checks and monitoring

### 3. Consistency Models
- CAP Theorem (Consistency, Availability, Partition Tolerance)
- Strong vs Eventual consistency
- ACID vs BASE properties
- Distributed transactions and consensus protocols (Raft, Paxos)

### 4. Architecture Patterns
- Microservices vs Monolith
- Event-driven architecture
- API Gateway pattern
- Service mesh
- CQRS (Command Query Responsibility Segregation)

### 5. Database Concepts
- SQL vs NoSQL databases
- Indexing strategies
- Read replicas
- Connection pooling

### 6. Networking Fundamentals
- DNS, CDN, Load balancers
- HTTP/HTTPS, REST, GraphQL
- WebSockets, gRPC
- Firewalls, DDoS protection

## Common System Design Questions

### Beginner Level
1. Design a URL Shortener (like TinyURL)
2. Design a Rate Limiter
3. Design a Web Crawler
4. Design a Twitter-like system
5. Design Instagram
6. Design Facebook Newsfeed

### Intermediate Level
7. Design a Chat Application (like WhatsApp)
8. Design a Video Streaming Service (like YouTube/Netflix)
9. Design a Ride-sharing App (like Uber/Lyft)
10. Design an E-commerce Platform (like Amazon)
11. Design a File Storage System (like Dropbox/Google Drive)
12. Design a Search Engine (like Google)

### Advanced Level
13. Design a Distributed Cache System
14. Design a Message Queue (like Kafka/RabbitMQ)
15. Design a Payment System
16. Design a Recommendation System
17. Design a Gaming Leaderboard
18. Design a Online Booking System (like Airbnb)

## Preparation Framework

### Step 1: Clarify Requirements
- Functional requirements (what the system should do)
- Non-functional requirements (performance, scalability, availability)
- Constraints and assumptions

### Step 2: High-Level Design
- Draw core components and their interactions
- Identify key APIs and data flows
- Consider technology choices

### Step 3: Deep Dive
- Focus on 2-3 critical components
- Discuss trade-offs and alternatives
- Address bottlenecks and failure scenarios

### Step 4: Wrap Up
- Summarize the design
- Identify potential improvements
- Answer follow-up questions

## Recommended Resources

### Books
1. "Designing Data-Intensive Applications" by Martin Kleppmann
2. "System Design Interview – An insider's guide" by Alex Xu
3. "Grokking the System Design Interview" by Design Gurus
4. "Clean Architecture" by Robert C. Martin

### Online Courses
1. [System Design Interview Course](https://www.educative.io/courses/grokking-the-system-design-interview) - Educative
2. [System Design Primer](https://github.com/donnemartin/system-design-primer) - GitHub
3. [AWS Architecture Center](https://aws.amazon.com/architecture/) - Amazon Web Services
4. [Google Cloud Architecture Center](https://cloud.google.com/architecture) - Google Cloud

### Websites & Blogs
1. [High Scalability](http://highscalability.com/)
2. [Martin Fowler's Blog](https://martinfowler.com/)
3. [Netflix Tech Blog](https://netflixtechblog.com/)
4. [Uber Engineering Blog](https://eng.uber.com/)
5. [Airbnb Engineering Blog](https://medium.com/airbnb-engineering)

### YouTube Channels
1. [Gaurav Sen](https://www.youtube.com/c/GauravSen)
2. [Tech Dummies Narendra L](https://www.youtube.com/c/TechDummiesNarendraL)
3. [ByteByteGo](https://www.youtube.com/c/ByteByteGo)
4. [Exponent](https://www.youtube.com/c/Exponent)

## Practice Questions with Frameworks

### 1. Design Twitter
**Core Features:**
- Post tweets
- Follow/unfollow users
- View timeline (home feed)
- Search tweets

**Key Components:**
- User service
- Tweet service
- Follow service
- Timeline generation service
- Cache layer (Redis)
- Database (PostgreSQL/Cassandra)
- Message queue (for async processing)

### 2. Design URL Shortener
**Core Features:**
- Generate short URL from long URL
- Redirect from short URL to original URL
- Custom aliases
- Analytics (click tracking)

**Key Components:**
- API service
- Hash generation service (Base62 encoding)
- Database storage
- Cache layer
- Redirect service

### 3. Design Chat Application
**Core Features:**
- One-to-one messaging
- Group chats
- Online/offline status
- Message persistence
- Media sharing

**Key Components:**
- WebSocket servers
- Message queue
- User presence service
- Message storage
- File storage service
- Notification service

## Daily Study Plan (Days 7-9)

### Day 7: Fundamentals Review
- CAP Theorem, Consistency models
- Load balancing, Caching
- Database basics (SQL vs NoSQL)

### Day 8: Common Patterns
- Microservices architecture
- API design (REST vs GraphQL)
- Event-driven systems
- Message queues

### Day 9: Full System Design Practice
- Practice 2-3 system design problems
- Focus on trade-offs and scalability
- Prepare to explain your reasoning clearly

## Quick Reference Cheat Sheet

### Consistency Models
- **Strong Consistency**: All nodes see same data at same time
- **Eventual Consistency**: Nodes will converge to same state eventually
- **Read-After-Write**: User sees their own writes immediately
- **Monotonic Reads**: If you read a value, future reads return same or newer value

### Load Balancing Algorithms
- **Round Robin**: Distribute requests sequentially
- **Least Connections**: Send to server with fewest active connections
- **IP Hash**: Hash client IP to determine server
- **Weighted Round Robin**: Assign weights to servers based on capacity

### Caching Strategies
- **Cache-Aside**: Application manages cache population
- **Write-Through**: Write to cache and database simultaneously
- **Write-Behind**: Write to cache first, async write to database
- **Refresh-Ahead**: Proactively refresh cache before expiration

### Database Patterns
- **Sharding**: Horizontal partitioning by key range/hash
- **Replication**: Master-slave or master-master setup
- **Indexing**: B-tree, Hash, Bitmap indexes
- **Connection Pooling**: Reuse database connections

---
*Last updated: $(date)*