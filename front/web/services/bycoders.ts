import http from '@/services/http';

class ByCoderService {
  listEntries(): Promise<any> {
    return http.get('/api/byCoders/list/all').then((response) => {
      return response;
    });
  }

  listStoreTransactions(storeId: number): Promise<any> {
    return http.get(`/api/byCoders/list/${storeId}`).then((response) => {
      return response;
    });
  }

  upload(file: any) {
    const formData = new FormData();
    formData.append('file', file);
    return http.post('/api/byCoders/upload', formData, {
      headers: {
        'Content-Type': 'multipart/forma-data',
      },
    });
  }
}

export default new ByCoderService();
