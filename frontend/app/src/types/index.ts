// Referenced from https://github.com/uiuc-apartments/uiuc-apartments.com
export interface Article {
    address: string
    apartment: string
    available_date: string
    bathrooms: number
    bedrooms: number
    id: number
    is_studio: boolean
    link: string
    rent: number
    latitude: number
    longitude: number
    listing_type?: 'apartment_complex' | 'individual_landlord' | 'sublease'
  }

  export type Filter = {
    minBedrooms: number
    maxBedrooms: number
    minBathrooms: number
    maxBathrooms: number
    // dateRange: Array<Date>
    minRent: number
    maxRent: number
    proximity: string
    selectedApartments: Array<string>
    listingTypes: Array<string>
  }