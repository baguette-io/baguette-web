FROM quay.io/baguette.io/baguette-base:latest
USER 1890
RUN git clone https://github.com/baguette-io/baguette-web.git /home/baguette/baguette-web
WORKDIR /home/baguette/baguette-web
RUN npm install --save
RUN npm run build
CMD ["npm", "start"]
