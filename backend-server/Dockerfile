# Use official Node.js image
FROM node:22

# Set working directory
WORKDIR /app

# Copy rest of the app files
COPY . .

RUN npm install package.json

# Expose Express port
EXPOSE 3000

# Run the Express server
CMD ["node", "index.js"]
