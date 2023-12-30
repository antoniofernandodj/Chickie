export class Response201Wrapper {
  uuid: string;
  constructor(response: any) {
    this.uuid = response.uuid;
  }
}
