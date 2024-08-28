import redis from 'redis';

const redisClient = redis.createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  redisClient.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  redisClient.get(schoolName, redis.print);
};
