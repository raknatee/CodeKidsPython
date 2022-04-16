FROM node:16-buster

WORKDIR /home/src/docs

COPY ./container-src/package.json .
RUN yarn install

CMD tail -f /dev/null