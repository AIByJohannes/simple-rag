# Use an official Node.js runtime as a parent image
FROM node:18-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY web/package.json web/package-lock.json* ./

# Install project dependencies
RUN npm install

# Copy the rest of the web application code
COPY web/ .

# Build the React application for production
RUN npm run build

# Install a simple HTTP server globally
RUN npm install -g serve

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Command to serve the static files from the dist folder
CMD ["serve", "-s", "dist", "-l", "3000"]
