import axios from 'axios';

export const fetchRaspberryPis = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/devices');
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis:', error);
    throw error;
  }
};
