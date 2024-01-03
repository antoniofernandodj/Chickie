export type UploadImageDataResponse = {
  loja_uuid: string | null
  data: {
    api_key: string;
    asset_id: string;
    bytes: number;
    created_at: string;
    etag: string;
    folder: string;
    format: string;
    height: number;
    original_filename: string;
    placeholder: boolean;
    public_id: string;
    resource_type: string;
    secure_url: string;
    signature: string;
    tags: string[];
    type: string;
    url: string;
    version: number;
    version_id: string;
    width: number;
  }
}
