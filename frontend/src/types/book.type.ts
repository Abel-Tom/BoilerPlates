export interface BookBase {
    title: string,
    author: string,
    isbn: string,

}

export interface CreateBookForm extends BookBase {
    published_date: Date
}

export interface CreateBookPayload extends BookBase {
    published_date: string
}

export interface Book extends CreateBookPayload {
    id: string
}

export interface BookResponse {
    total: number,
    page: number,
    per_page: number,
    books: Book[]
}

export interface CreateBookResponse extends Book {
    user_id: string
}

export interface BookFilters {
    title: string,
    author: string
    start_date: Date,
    end_date: Date,
    page: number,
    per_page: number
}


