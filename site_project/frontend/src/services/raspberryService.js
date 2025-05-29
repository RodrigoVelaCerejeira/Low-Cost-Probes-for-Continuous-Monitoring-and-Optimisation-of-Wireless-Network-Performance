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

export const fetchFailuresLastDay = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/lastday');
    return response.data;
  } catch (error) {
    console.error('Error finding Raspberry Pis with failures in the last day:', error);
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

export const fetchExcelData = async () => {
  try {
    const response = await axios.get('http://192.92.147.85:3001/raspberry/excel', {
      responseType: 'blob', 
    });

    const blob = new Blob([response.data], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });

    const url = window.URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'dados_rede.xlsx');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);

  } catch (error) {
    console.error('Error exporting data:', error);
    throw error;
  }
};

export const fetchRaspberryDataById = async (id) => {
  try {
    const response = await axios.get(`http://192.92.147.85:3001/raspberry/excel/${id}` , {
    responseType: 'blob',
    });

    const blob = new Blob([response.data], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });

    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `dados_rede_${id}.xlsx`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);

  } catch (error) {
    console.error('Error exporting data:', error);
    throw error;
  }
};
