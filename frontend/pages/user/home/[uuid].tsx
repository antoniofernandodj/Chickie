'use client'
import { useRouter } from 'next/router'

export default function Page() {
    const router = useRouter()
    console.log({router: router.query})
    return (
        <p>Post</p>
    )
}
