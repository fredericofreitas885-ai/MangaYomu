#!/usr/bin/env python3
"""Localize the MangaYomu Android interface into Portuguese (Portugal)."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("app/src/main")
D = "$"
T = {
"Explore":"Explorar", "Library":"Biblioteca", "History":"Histórico",
"Downloads":"Transferências", "Settings":"Definições", "Search":"Pesquisar",
"Loading…":"A carregar…", "Something went wrong. Please try again.":"Ocorreu um erro. Tenta novamente.",
"No internet connection. Please check your network.":"Sem ligação à Internet. Verifica a ligação.",
"Retry":"Tentar novamente", "Cancel":"Cancelar", "Save":"Guardar", "Delete":"Eliminar",
"Share":"Partilhar", "Back":"Voltar", "Error":"Erro", "Clear":"Limpar", "Add":"Adicionar", "All":"Todos",
"Popular":"Populares", "Latest":"Recentes", "Sources":"Fontes", "Search manga…":"Pesquisar mangás…",
"Type to search manga":"Escreve para pesquisar mangás", "No manga found":"Não foram encontrados mangás",
"Error loading manga":"Erro ao carregar os mangás",
"Failed to load popular manga":"Não foi possível carregar os mangás populares",
"Failed to load latest manga":"Não foi possível carregar os mangás recentes", "Search failed":"A pesquisa falhou",
"Clear search":"Limpar pesquisa", "My Library":"A minha biblioteca",
"Your library is empty. Add manga from Explore!":"A tua biblioteca está vazia. Adiciona mangás em Explorar!",
"Your library is empty.\\nExplore and add some manga!":"A tua biblioteca está vazia.\\nExplora e adiciona alguns mangás!",
"New Category":"Nova categoria", "Category name":"Nome da categoria", "Add category":"Adicionar categoria",
"Reading History":"Histórico de leitura", "No reading history yet":"Ainda não existe histórico de leitura",
"No reading history yet.":"Ainda não existe histórico de leitura.", "Clear History":"Limpar histórico",
"Are you sure you want to clear your entire reading history?":"Tens a certeza de que queres limpar todo o histórico de leitura?",
"Clear all history":"Limpar todo o histórico", "Remove entry":"Remover registo",
"No downloads yet":"Ainda não existem transferências",
"No downloads in progress or queued.":"Não existem transferências em curso nem na fila.",
"Queued":"Na fila", "Completed":"Concluído", "Ongoing":"Em publicação", "Hiatus":"Em pausa",
"Cancelled":"Cancelado", "Unknown":"Desconhecido", "Cancel or delete":"Cancelar ou eliminar",
"General":"Geral", "Appearance":"Aparência", "Reading":"Leitura", "About":"Sobre",
"System Default":"Predefinição do sistema", "Light":"Claro", "Dark":"Escuro",
"Default Reading Mode":"Modo de leitura predefinido", "Manga Sources & Sites":"Fontes e sites de mangá",
"Add New Manga Site":"Adicionar novo site de mangá",
"Configure a new website source with CSS selectors:":"Configura uma nova fonte de site com seletores CSS:",
"Source Name (e.g. MangaSee)":"Nome da fonte (ex.: MangaSee)",
"Base URL (e.g. https://mangasee123.com)":"URL base (ex.: https://mangasee123.com)",
"Popular path":"Caminho dos populares", "Search path":"Caminho da pesquisa",
"Manga item selector":"Seletor do elemento de mangá", "Title selector":"Seletor do título",
"Cover img selector":"Seletor da imagem da capa", "Add Source":"Adicionar fonte", "Add Site":"Adicionar site",
"Remove source":"Remover fonte", "MangaYomu v1.0.0":"MangaYomu v1.0.0",
"A modern, open-source manga reader app for Android inspired by Kotatsu. Built with Jetpack Compose, Room Database, Kotlin Coroutines, and an extensible multi-source engine.":"Uma aplicação moderna e de código aberto para ler mangás no Android, inspirada no Kotatsu. Desenvolvida com Jetpack Compose, Room Database, Kotlin Coroutines e um sistema extensível de várias fontes.",
"Manga Details":"Detalhes do mangá", "In Library":"Na biblioteca", "Add to Library":"Adicionar à biblioteca",
"Download All":"Transferir tudo", "Description":"Descrição", "Downloaded":"Transferido",
"Download chapter":"Transferir capítulo", "Chapters":"Capítulos", "Start Reading":"Começar a ler",
"Continue Reading":"Continuar a ler", "Reading Mode":"Modo de leitura",
"Left to Right":"Da esquerda para a direita", "Right to Left":"Da direita para a esquerda",
"Webtoon":"Webtoon", "Previous Chapter":"Capítulo anterior", "Next Chapter":"Próximo capítulo",
"Chapter":"Capítulo", "Manga":"Mangá", "Sort By":"Ordenar por", "Alphabetical":"Ordem alfabética",
"Unknown Title":"Título desconhecido", "Response body is null":"A resposta do servidor está vazia",
"Failed to load chapter pages":"Não foi possível carregar as páginas do capítulo",
"Failed to load manga details":"Não foi possível carregar os detalhes do mangá",
}
T.update({
"Library ("+D+"{uiState.libraryManga.size})":"Biblioteca ("+D+"{uiState.libraryManga.size})",
"Downloads ("+D+"{downloads.size})":"Transferências ("+D+"{downloads.size})",
"Chapter "+D+"{chapter.chapterNumber}":"Capítulo "+D+"{chapter.chapterNumber}",
D+"{uiState.chapters.size} Chapters":D+"{uiState.chapters.size} capítulos",
D+"{uiState.readingMode.label} • Page "+D+"{uiState.currentPage + 1} / "+D+"{uiState.pages.size}":D+"{uiState.readingMode.label} • Página "+D+"{uiState.currentPage + 1} / "+D+"{uiState.pages.size}",
"Page "+D+"{index + 1}":"Página "+D+"{index + 1}",
"Page "+D+"{actualIndex + 1}":"Página "+D+"{actualIndex + 1}",
D+"{entry.chapter.chapterNumber}":"Capítulo "+D+"{entry.chapter.chapterNumber}",
"Chapter "+D+"{index + 1}":"Capítulo "+D+"{index + 1}",
})
PREFIX = {
'"Search manga in ': '"Pesquisar mangás em ',
'"Language: ': '"Idioma: ', '"Author: ': '"Autor: ',
'"Artist: ': '"Ilustrador: ', '"Status: ': '"Estado: ',
'"Source: ': '"Fonte: ', '"Source not found: ': '"Fonte não encontrada: ',
'"Page ': '"Página ', '"Chapter ': '"Capítulo ',
'"HTTP error ': '"Erro HTTP ', '"Empty response body from ': '"A resposta do servidor está vazia em ', '"MangaDex API error ': '"Erro da API do MangaDex ', '"Failed to parse MangaDex response from ': '"Não foi possível interpretar a resposta do MangaDex de ', '"Failed to download image: ': '"Não foi possível transferir a imagem: ',
}
def translate_kotlin():
    for p in (ROOT / "java/com/mangayomu").rglob("*.kt"):
        old = p.read_text(encoding="utf-8")
        new = old
        for a, b in T.items():
            new = new.replace('"' + a + '"', '"' + b + '"')
        for a, b in PREFIX.items():
            new = new.replace(a, b)
        new = new.replace(
          'SimpleDateFormat("MMM dd, yyyy HH:mm", Locale.getDefault())',
          'SimpleDateFormat("dd/MM/yyyy HH:mm", Locale("pt", "PT"))')
        if new != old:
            p.write_text(new, encoding="utf-8")

def translate_resources():
    p = ROOT / "res/values/strings.xml"
    tree = ET.parse(p)
    R = {
"nav_explore":"Explorar","nav_library":"Biblioteca","nav_history":"Histórico",
"nav_downloads":"Transferências","nav_settings":"Definições","search":"Pesquisar",
"loading":"A carregar…","error_generic":"Ocorreu um erro. Tenta novamente.",
"error_network":"Sem ligação à Internet. Verifica a ligação.","retry":"Tentar novamente",
"cancel":"Cancelar","ok":"OK","save":"Guardar","delete":"Eliminar","share":"Partilhar","back":"Voltar",
"explore_title":"Explorar mangás","explore_search_hint":"Pesquisar mangás…",
"explore_no_results":"Não foram encontrados mangás","library_title":"A minha biblioteca",
"library_empty":"A tua biblioteca está vazia. Adiciona mangás em Explorar!",
"history_title":"Histórico de leitura","history_empty":"Ainda não existe histórico de leitura",
"history_clear":"Limpar histórico","downloads_title":"Transferências",
"downloads_empty":"Ainda não existem transferências","settings_title":"Definições",
"settings_general":"Geral","settings_appearance":"Aparência","settings_reading":"Leitura",
"settings_downloads":"Transferências","settings_about":"Sobre",
"manga_add_to_library":"Adicionar à biblioteca","manga_in_library":"Na biblioteca",
"manga_chapters":"Capítulos","manga_description":"Descrição","manga_start_reading":"Começar a ler",
"manga_continue_reading":"Continuar a ler","reader_chapter":"Capítulo %1$s",
"reader_next_chapter":"Próximo capítulo","reader_previous_chapter":"Capítulo anterior"}
    for el in tree.getroot().findall("string"):
        if el.get("name") in R:
            el.text = R[el.get("name")]
    tree.write(p, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    translate_kotlin()
    translate_resources()
    print("Interface do MangaYomu traduzida para português (Portugal).")
