export class Response201Wrapper {
  uuid: string;
  constructor(response: any) {
    this.uuid = response.uuid;
  }
}



export class Response201ImageCreatedWrapper {
  uuid: string;
  image_url: string
  constructor(response: any) {
    this.uuid = response.uuid;
    this.image_url = response.image_url
  }
}
