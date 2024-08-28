import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);

const setNewSchool = (schoolName, value) => {
  redisClient.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    console.log(await getAsync(schoolName));
  } catch (error) {
    console.error(error);
  }
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

redisClient.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

redisClient.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
