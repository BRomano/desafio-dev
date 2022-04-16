import http from '@/services/http';

class ByCoderService {
  listEntries(): Promise<any> {
    return http.get('/byCoders/list').then((response) => {
      return response;
    });
  }

  upload(file: any) {
    const formData = new FormData();
    formData.append('file', file);
    return http.post('/byCoders/upload', formData, {
      headers: {
        'Content-Type': 'multipart/forma-data',
      },
    });
  }
}

export default new ByCoderService();
