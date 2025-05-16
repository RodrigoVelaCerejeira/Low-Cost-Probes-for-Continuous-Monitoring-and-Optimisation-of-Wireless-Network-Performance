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

export const fetchRaspberryById = async (id) => {
  try {
    const response = await axios.get(`http://192.92.147.85:3001/raspberry/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry:', error);
    throw error;
  }
};

export const fetchNullRaspberries = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/nulls');
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis with null values:', error);
    throw error;
  }
};

export const fetchFailuresLastHour = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/lasthour');
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis with failures in the last hour:', error);
    throw error;
  }
};

export const fetchAPs = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/aps');
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis with null values:', error);
    throw error;
  }
};

export const fetchAPsById = async (id) => {
  try {
    const response = await axios.get(`http://192.92.147.85:3001/raspberry/aps/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry:', error);
    throw error;
  }
};
