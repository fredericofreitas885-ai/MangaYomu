# 📖 MangaYomu — Leitor de Mangá Android (Semelhante ao Kotatsu)

**MangaYomu** é um aplicativo Android nativo construído com **Kotlin** e **Jetpack Compose**, inspirado no leitor de mangá de código aberto **Kotatsu**. O aplicativo conta com arquitetura moderna MVVM (Clean Architecture), banco de dados local com Room, suporte a leitura offline e um **sistema multi-fontes extensível** que permite adicionar sites e catálogos facilmente.

---

## 🌟 Principais Funcionalidades

### 1. 🔍 Explorar & Buscar
* **Múltiplos Catálogos:** Alterne instantaneamente entre fontes de mangá (MangaDex, MangaKakalot e fontes personalizadas).
* **Abas de Descoberta:** Navegue por *Populares*, *Recentes (Latest)* e *Busca*.
* **Busca Global:** Encontre qualquer obra por título.
* **Paginação Infinita:** Carregamento suave e contínuo ao rolar a grade.

### 2. 📖 Leitor Completo (Reader)
* **3 Modos de Leitura:**
  * **Direita para Esquerda (RTL):** Leitura tradicional japonesa de mangás.
  * **Esquerda para Direita (LTR):** Leitura ocidental.
  * **Webtoon:** Rolagem vertical contínua otimizada para Manhwa e Webtoons.
* **Controles Imersivos:** Toque no centro da tela para alternar a interface de controles.
* **Barra de Progresso & Slider:** Pule rapidamente para qualquer página.
* **Troca Rápida de Capítulos:** Botões de próximo/anterior capítulo integrados.
* **Progresso Automático:** Salva a última página lida automaticamente.

### 3. 📚 Biblioteca & Categorias
* **Favoritos:** Salve seus mangás prediletos na biblioteca local.
* **Categorias Personalizadas:** Crie suas próprias categorias (ex: *Lendo*, *Completos*, *Favoritos*, *Plano para Ler*).
* **Filtros por Aba:** Filtre seus mangás por categoria em abas deslizáveis.

### 4. 📥 Gerenciador de Downloads (Leitura Offline)
* **Fila de Downloads:** Baixe capítulos individuais ou todos os capítulos de uma vez.
* **Progresso em Tempo Real:** Acompanhe o percentual e status de cada download.
* **Modo Offline Automático:** O leitor detecta se o capítulo já foi baixado e carrega as imagens do armazenamento local sem usar internet.

### 5. 📜 Histórico de Leitura
* Histórico cronológico com data, hora, capa e capítulo lido.
* Opção de continuar a leitura de onde parou.
* Limpeza de histórico individual ou total.

### 6. 🔌 Sistema Extensível de Fontes & Sites (Como Adicionar Novas Fontes)
O MangaYomu foi projetado para ser **100% extensível**:

#### A. Adicionar pelo próprio aplicativo (via UI)
1. Vá na aba **Settings**.
2. Clique no botão **"Add Site"** na seção *Manga Sources & Sites*.
3. Insira o nome do site, URL base, caminho de busca e os seletores CSS (ex: `.manga-item`, `.title a`, `img`).
4. O app passa a usar o site instantaneamente no Explore!

#### B. Adicionar no código (Kotlin + Jsoup)
Basta criar uma classe herdando de `HttpSource` (para raspagem HTML com Jsoup) ou implementando `MangaSource` (para APIs REST):

```kotlin
class MeuSiteMangaSource @Inject constructor(
    override val client: OkHttpClient
) : HttpSource() {
    override val id = "meusite"
    override val name = "Meu Site de Mangás"
    override val language = "pt-br"
    override val baseUrl = "https://meusite.com"

    override suspend fun getPopularManga(page: Int): MangaPage {
        val doc = fetchDocument("$baseUrl/populares?p=${page + 1}")
        val mangas = doc.select(".card-manga").map { el ->
            Manga(
                id = el.selectAttr("a", "href").substringAfterLast("/"),
                title = el.selectText(".titulo"),
                coverUrl = el.selectAttr("img", "src"),
                sourceId = id
            )
        }
        return MangaPage(mangas, hasNextPage = true)
    }

    // getLatestManga, searchManga, getChapterList, getPageList...
}
```
E registrá-la em `SourceManager.kt`!

---

## 🛠️ Stack Tecnológica

| Componente | Tecnologia |
|---|---|
| **Linguagem** | Kotlin 1.9.20 |
| **UI** | Jetpack Compose + Material Design 3 |
| **Injeção de Dependência** | Hilt (Dagger) 2.48 com KSP |
| **Banco de Dados Local** | Room Database 2.6.1 |
| **Carregamento de Imagens** | Coil Compose 2.5.0 |
| **Rede & HTTP** | OkHttp 4.12.0 + Retrofit 2.9.0 |
| **HTML Scraping** | Jsoup 1.17.2 |
| **Serialização** | Gson 2.10.1 |
| **Concorrência** | Coroutines & StateFlow / Flow |
| **Navegação** | Compose Navigation |

---

## 📂 Estrutura do Projeto

```
app/src/main/java/com/mangayomu/
├── MainActivity.kt                # Ponto de entrada com tema Edge-to-Edge
├── MangaYomuApp.kt                # Application class com @HiltAndroidApp
├── data/
│   ├── database/                  # Room: AppDatabase, DAOs e Entidades
│   │   ├── dao/                   # MangaDao, ChapterDao, HistoryDao, CategoryDao
│   │   └── entity/                # MangaEntity, ChapterEntity, HistoryEntity, CategoryEntity
│   ├── download/                  # DownloadManager (Fila de downloads em disco)
│   ├── network/                   # Modelos de resposta REST da API do MangaDex
│   ├── repository/                # Implementações dos repositórios
│   └── source/                    # Motor de fontes: MangaDexSource, MangaKakalotSource, CustomScraperSource
├── domain/
│   ├── model/                     # Manga, Chapter, Page, Category, HistoryEntry
│   └── repository/                # Interfaces limpas de repositório
├── di/                            # Módulos Hilt (Database, Network, Repositories, Sources)
└── ui/
    ├── components/                # Componentes compartilhados (MangaGridItem, SearchBar, ErrorMessage...)
    ├── details/                   # Tela de detalhes do mangá e lista de capítulos
    ├── downloads/                 # Tela de gerenciamento de downloads
    ├── explore/                   # Tela de exploração, catálogo e busca
    ├── history/                   # Tela de histórico de leitura
    ├── library/                   # Tela de biblioteca e favoritos
    ├── navigation/                # Bottom Navigation Bar e Rotas (NavHost)
    ├── reader/                    # Leitor interativo (RTL, LTR, Webtoon)
    ├── settings/                  # Configurações e adição de novas fontes
    └── theme/                     # Tema Material 3
```

---

## 🚀 Como Executar no Android Studio

1. Abra o **Android Studio**.
2. Selecione **Open** e aponte para a pasta:
   `C:\Users\DELL\.gemini\antigravity\scratch\MangaYomu`
3. Aguarde o **Gradle Sync** concluir o download das dependências.
4. Conecte um dispositivo Android físico com depuração USB ou inicie um Emulador (Android 8.0+ / API 26 ou superior).
5. Clique no botão **Run (Shift + F10)**.
