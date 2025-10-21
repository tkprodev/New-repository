# Pet Super App

This repository contains a minimal starter project for a pet super application.
It is divided into a server (Node.js/Express) and a client (React) folder.

## Prerequisites
- Node.js 18+
- npm

## Setup
1. Install dependencies for both the server and client:
   ```bash
   cd server && npm install
   cd ../client && npm install
   ```
2. Start the server:
   ```bash
   cd server
   npm start
   ```
3. In another terminal, start the client development server:
   ```bash
   cd client
   npm start
   ```

The client is configured to proxy API requests to the server. Open `http://localhost:8080`
(or the port shown in the console) to view the application.
