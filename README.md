# elastic-search-in-django

## Prerequisites

Before running this project, ensure that Elasticsearch is running on your local machine. If Elasticsearch is not already installed and running, follow the setup instructions below.

## Installation and Setup

Visit the [Elasticsearch Downloads](https://www.elastic.co/downloads/elasticsearch) or [Elasticsearch pypi](https://pypi.org/project/elasticsearch/) page to get started. There are two methods to run Elasticsearch:

### Method 1: Using Docker (Recommended)

If Docker is installed on your machine, run the following command in your terminal:

```bash
curl -fsSL https://elastic.co/start-local | sh
```

Once the container is running, verify the installation by visiting:
- Elasticsearch API: [http://localhost:9200/](http://localhost:9200/)
- Kibana UI: [http://localhost:5601/](http://localhost:5601/)

### Method 2: Manual Installation

1. Download the Elasticsearch ZIP file and extract it to your desired location
2. Navigate to the `config` folder and open `elasticsearch.yml` in a text editor
3. Add the following line at the end of the file:
   ```
   xpack.security.enabled: false
   ```
4. Save the file and close the editor
5. Navigate to the `bin` folder, open a terminal, and run:
   ```bash
   elasticsearch.bat
   ```
6. Verify the installation by visiting [http://localhost:9200/](http://localhost:9200/)