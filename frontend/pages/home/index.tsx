'use client'
import axios from 'axios';
import Image from 'next/image'
import { useState, useEffect } from 'react';

// Interface para representar o formato dos dados do Pokémon
interface PokemonData {
    name: string;
    sprites: {
        front_default: string;
    };
}



export async function getData(): Promise<PokemonData[]> {
    const pokemons = [];
    const urlBase = "https://pokeapi.co/api/v2/pokemon/";

    try {
        for (let i = 1; i < 9; i++) {
            const url = urlBase + `${i}`;
            const response = await axios.get(url);
            pokemons.push(response.data);
        }
    } catch (error) {
        console.error("Erro ao buscar dados dos Pokémon:", error);
    }

    return pokemons;
}


export default function Home() {
    const [pokemons, setPokemons] = useState<PokemonData[]>([]);

    useEffect(() => {
        async function fetchPokemons() {
            const data = await getData();
            setPokemons(data);
        }
        fetchPokemons();
    }, []);

    const pkmn = pokemons.map(pokemon => (
        <div key={pokemon.name}>
            <div>{pokemon.name}</div>
            <Image alt={pokemon.name} width={300} height={240}
            src={pokemon.sprites.front_default} />
        </div>
    ));

    return (
        <div>
            {pkmn}
        </div>
    );
}
