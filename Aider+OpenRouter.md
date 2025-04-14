# Aider与OpenRouter开发项目手册

## 关键要点
- **Aider简介**：Aider 是一个 AI 驱动的编码助手，可通过在代码中添加特定注释（如 `# AI`）来帮助编写和修改代码。
- **OpenRouter功能**：OpenRouter 提供统一接口，允许访问多种大型语言模型（LLMs），并根据价格和性能优化选择。
- **结合优势**：使用 Aider 和 OpenRouter，开发者可以灵活选择适合项目的模型，提升编码效率。
- **设置简单**：需要安装 Aider、获取 OpenRouter API 密钥并进行基本配置。
- **需注意**：模型选择和令牌成本可能影响使用体验，建议根据项目需求调整。

### 什么是 Aider?

Aider 是一个命令行工具，充当 AI 结对程序员。它允许你直接在终端中与 GPT-3.5/GPT-4 (或其他兼容模型) 协同工作，请求代码更改、编写新功能、修复 Bug 或生成测试。Aider 的核心优势在于它能够理解你的本地代码库上下文，直接编辑本地文件，并与 Git 集成，自动提交有意义的变更。

### 什么是 OpenRouter?

OpenRouter 是一个 API 聚合器和路由器，它提供了一个统一的接口来访问来自不同提供商 (如 OpenAI, Anthropic, Google, Mistral AI, Meta 等) 的各种大型语言模型 (LLM)。用户可以通过一个 OpenRouter API Key 访问多种模型，通常具有更灵活的定价和模型选择。

### 如何开始？
要使用 Aider 和 OpenRouter，您需要安装 Aider，获取 OpenRouter API 密钥，并配置环境。以下是基本步骤：
1. 使用 `pip` 安装 Aider。
2. 在 OpenRouter 网站注册并获取 API 密钥。
3. 设置环境变量以使用密钥。
4. 运行 Aider 并指定 OpenRouter 模型。

### 为什么结合使用 Aider 和 OpenRouter?

将 Aider 与 OpenRouter 结合使用，可以带来以下好处：

1.  **模型选择多样性**: 不再局限于 OpenAI 的模型，可以根据任务需求、性能偏好或成本考虑，轻松切换使用 Claude, Gemini, Llama, Mistral 等多种先进模型。
2.  **潜在成本优化**: OpenRouter 提供不同模型的不同定价，有时可能比直接使用原始提供商更具成本效益，或者可以访问免费或低成本的优秀模型。
3.  **访问最新模型**: OpenRouter 通常会快速集成最新的流行模型，让你能第一时间在 Aider 中体验它们。
4.  **统一管理**: 只需管理一个 OpenRouter API Key 即可访问众多模型，简化了密钥管理。

---

## 详细手册

### 引言

Aider 是一个强大的 AI 编码助手，可直接在终端或 IDE 中运行，通过解析代码中的特定注释（如 `# AI`、`# AI!` 或 `# AI?`）来实现代码生成、修改或问题解答。OpenRouter 则是一个统一的 API 平台，允许用户访问多种大型语言模型（LLMs），如 Anthropic 的 Claude 系列或 DeepSeek 的模型，并根据价格、延迟和吞吐量自动选择最佳提供商。

结合 Aider 和 OpenRouter，开发者可以利用多种 LLMs 的能力来加速项目开发，同时保持对模型选择和成本的控制。本手册将详细介绍如何设置和使用这一组合，包括安装、配置、实际操作以及最佳实践。

### 前提条件

#### 1. 安装 Aider
要开始使用 Aider，您需要安装它并确保 Python 环境兼容。推荐使用 Python 3.12。以下是安装步骤：

- **通过 pipx 安装**（推荐，以隔离环境）：
  ```bash
  brew install [email protected]
  brew install pipx
  pipx install --python python3.12 aider-chat
  ```
- **通过 pip 安装**：
  ```bash
  python -m pip install -U aider-chat
  ```
- These one-liners will install aider, along with python 3.12 if needed. They are based on the uv installers.

Windows

```
powershell -ExecutionPolicy ByPass -c "irm https://aider.chat/install.ps1 | iex"
```

Mac & Linux

Use curl to download the script and execute it with sh:
```bash
curl -LsSf https://aider.chat/install.sh | sh
```

If your system doesn’t have curl, you can use wget:

``` bash
wget -qO- https://aider.chat/install.sh | sh
```

- 确保 Python 版本在 3.8 至 3.13 之间。更多安装详情请参考 [Aider 安装指南](https://aider.chat/docs/install.html)。



#### 2. 获取 OpenRouter API 密钥
OpenRouter 提供对多种 LLMs 的访问，您需要一个 API 密钥来连接 Aider：
- 访问 [OpenRouter 网站](https://openrouter.ai/) 并注册账户。
- 在账户设置的“API Keys”部分生成一个新的 API 密钥。
- 妥善保存密钥，因为它将用于配置 Aider。

### 配置

#### 1. 设置 OpenRouter API 密钥
为了让 Aider 使用 OpenRouter 的模型，您需要设置环境变量 `OPENROUTER_API_KEY`。以下是不同操作系统的设置方法：

- **Mac/Linux**：
  ```bash
  export OPENROUTER_API_KEY=<your_api_key>
  ```
  为确保密钥在每次终端会话中可用，可将其添加到 `~/.zshrc` 或 `~/.bashrc`：
  ```bash
  echo 'export OPENROUTER_API_KEY=<your_api_key>' >> ~/.zshrc
  source ~/.zshrc
  ```

- **Windows**：
  ```bash
  setx OPENROUTER_API_KEY <your_api_key>
  ```
  注意：设置后需要重启终端或命令提示符以应用更改。

- **增强安全性（Mac 示例）**：
  为避免直接暴露密钥，可以使用系统密钥链存储：
  ```bash
  zsh -f
  security add-generic-password -a "$USER" -s OPENROUTER_API_KEY -w "<your_api_key>"
  ```
  然后在 `~/.zshrc` 中添加：
  ```bash
  export OPENROUTER_API_KEY=$(security find-generic-password -a "$USER" -s OPENROUTER_API_KEY -w)
  ```
  最后刷新配置：
  ```bash
  source ~/.zshrc
  ```

#### 2. 配置提供商路由（可选）
OpenRouter 支持多个模型提供商，您可以控制 Aider 使用哪些提供商。配置方法包括：

- **在 OpenRouter 账户设置中忽略提供商**：
  登录 [OpenRouter 设置](https://openrouter.ai/settings/privacy)，在隐私设置中选择是否允许“可能使用输入数据进行训练的提供商”。

- **使用 `.aider.model.settings.yml` 文件**：
  在家目录或项目根目录创建 `.aider.model.settings.yml`，例如：
  ```yaml
  - name: openrouter/anthropic/claude-3.7-sonnet
    extra_params:
      extra_body:
        provider:
          order: ["Anthropic", "Together"]
          allow_fallbacks: false
          data_collection: "deny"
          require_parameters: true
  ```
  此配置指定优先使用 Anthropic 和 Together 提供商，禁用回退，拒绝数据收集，并要求支持所有参数。更多详情请参考 [OpenRouter 提供商路由文档](https://openrouter.ai/docs/provider-routing)。

### 使用方法

#### 1. 启动 Aider 并选择 OpenRouter 模型
启动 Aider 时，需指定 OpenRouter 模型，格式为 `openrouter/<provider>/<model>`。以下是一个示例命令：

```bash
aider --dark-mode --pretty --cache-prompts --no-auto-commits --model openrouter/openrouter/optimus-alpha
```

- **参数说明**：
  - `--dark-mode`：适配深色终端背景。
  - `--pretty`：优化输出格式。
  - `--cache-prompts`：启用模型支持的提示缓存。
  - `--no-auto-commits`：禁用自动提交，允许手动控制。
  - `--model`：指定模型，如 `openrouter/openrouter/optimus-alpha`。

- **列出可用模型**：
  要查看 OpenRouter 提供的模型列表，运行：
  ```bash
  aider --list-models openrouter/
  ```

#### 2. 与 Aider 交互
启动 Aider 后，您可以在终端或 IDE 中通过命令和代码注释与它交互。以下是常用操作：

- **命令**：
  | 命令            | 功能                              |
  |----------------|----------------------------------|
  | `/help`        | 显示所有可用命令                  |
  | `/add <filename>` | 将文件添加到聊天上下文（支持 Tab 自动完成） |
  | `/commit`      | 提交代码更改                      |
  | `/ask`         | 切换到问答模式                    |
  | `/architect`   | 切换到架构模式（用于高层规划）      |
  | `/model`       | 切换到其他模型                    |
  | `/tokens`      | 查看令牌使用情况                  |
  | `/clear`       | 清除聊天历史                      |
  | `/drop`        | 从上下文中移除特定文件             |

- **AI 注释**：
  在代码中添加注释以触发 Aider 的功能：
  - `# AI!`：请求修改代码。
  - `# AI?`：提出问题。
  - `# AI`：通用指令或添加文件到上下文。
  例如：
  ```python
  # AI: 编写一个计算阶乘的函数
  ```

- 更多命令和用法请参考 [Aider 命令文档](https://aider.chat/docs/usage/commands.html)。

#### 3. 处理模型警告和元数据
某些模型可能需要额外的元数据配置，以确保正确处理令牌限制和成本。编辑 `$HOME/.aider.model.metadata.json`，添加以下内容：

```json
{
  "openrouter/qwen/qwen2.5-coder-32k": {
    "max_tokens": 32768,
    "input_cost_per_token": 0.00000018,
    "output_cost_per_token": 0.00000018
  },
  "openrouter/deepseek/deepseek-chat": {
    "max_tokens": 8192,
    "input_cost_per_token": 0.00000014,
    "output_cost_per_token": 0.00000028
  }
}
```

此配置指定了最大令牌数和每令牌的输入/输出成本。更多故障排除信息请参考 [Aider 故障排除文档](https://aider.chat/docs/llms/warnings.html)。

### 示例

#### 示例 1：设置编码会话
假设您正在开发一个 Python 项目，需要编写一个函数。以下是步骤：

1. 进入项目目录：
   ```bash
   cd my_project
   ```
2. 启动 Aider：
   ```bash
   aider --model openrouter/openrouter/optimus-alpha
   ```
3. 添加文件：
   ```bash
   /add main.py
   ```
4. 在 `main.py` 中添加 AI 注释：
   ```python
   # AI: 编写一个计算阶乘的函数
   ```
   Aider 将生成类似以下代码：
   ```python
   def factorial(n):
       if n == 0:
           return 1
       return n * factorial(n - 1)
   ```

#### 示例 2：管理聊天上下文
在大型项目中，您可能需要管理多个文件和上下文：
- 检查令牌使用：
  ```bash
  /tokens
  ```
- 清除历史以减少令牌消耗：
  ```bash
  /clear
  ```
- 移除不必要的文件：
  ```bash
  /drop unused_file.py
  ```

#### 示例 3：使用不同模型
如果当前模型（如 Claude）不适合，您可以切换到 DeepSeek：
```bash
/model openrouter/deepseek/deepseek-chat
```

### 最佳实践和技巧

- **选择适合的模型**：
  - 对于编码任务，推荐使用 Anthropic 的 Claude 系列（如 `claude-3.5-sonnet`）或 DeepSeek 的模型（如 `deepseek-chat`），因为它们在代码生成方面表现优异。
  - 查看模型详情和成本请访问 [OpenRouter 模型列表](https://openrouter.ai/models)。

- **管理成本**：
  - 监控令牌使用情况，避免选择高成本模型（如某些高端模型每百万令牌可能高达数美元）。
  - 使用 `/tokens` 定期检查消耗。

- **优化性能**：
  - 在大型项目中，使用 `.aiderignore` 文件排除无关文件，减少上下文令牌。例如：
    ```
    node_modules/
    dist/
    ```
  - 参考 [Aider 大型项目优化](https://aider.chat/docs/faq.html)。

- **故障排除**：
  - 如果 OpenRouter 模型无响应，检查 API 密钥是否正确设置，或查看 [OpenRouter 仪表板](https://openrouter.ai/) 是否有 API 活动。
  - 常见问题请参考 [Aider 故障排除](https://aider.chat/docs/troubleshooting/models-and-keys.html)。

### 高级配置

#### 1. 使用 `.aider.conf.yml`
您可以通过 `.aider.conf.yml` 文件预设模型和密钥。例如：
```yaml
model: openrouter/openrouter/optimus-alpha
```
或为 DeepSeek 配置：
```yaml
model: openrouter/deepseek/deepseek-v3-base:free
```
将文件放置在家目录或项目根目录。

#### 2. 自定义模型设置
对于高级用户，可以在 `.aider.model.settings.yml` 中调整模型参数。例如，设置最大令牌数：
```yaml
- name: openrouter/anthropic/claude-3.5-sonnet
  extra_params:
    max_tokens: 8192
    cache_control: true
```
更多设置请参考 [Aider 高级模型设置](https://aider.chat/docs/config/adv-model-settings.html)。

### 常见问题解答

| 问题                              | 解决方法                                                                 |
|----------------------------------|------------------------------------------------------------------------|
| OpenRouter 模型无响应             | 确保 `OPENROUTER_API_KEY` 已正确设置，检查 [OpenRouter 仪表板](https://openrouter.ai/) 的 API 活动。 |
| 模型生成代码不符合预期             | 尝试切换模型（如从 Claude 到 DeepSeek）或提供更具体的 AI 注释。                     |
| 令牌成本过高                     | 检查 `/tokens` 输出，选择成本较低的模型，或优化上下文文件数量。                       |
| Aider 无法识别文件                | 使用 `/add` 命令显式添加文件，或检查文件路径是否正确。                               |

### 总结

通过 Aider 和 OpenRouter 的结合，开发者可以利用多种 LLMs 的能力来加速编码过程。本手册提供了从安装到高级配置的全面指导，帮助您快速上手并优化开发流程。无论是编写简单脚本还是开发复杂应用，这一组合都能提供强大的支持。

### 关键引用
- [Aider 官方文档 - 使用 OpenRouter 配置指南](https://aider.chat/docs/llms/openrouter.html)
- [Kubito 博客 - Aider 和 OpenRouter 的 AI 助手实践](https://kubito.dev/posts/ai-assistant-aider-openrouter/)
- [Aider 官方文档 - 模型和 API 密钥故障排除](https://aider.chat/docs/troubleshooting/models-and-keys.html)
- [Reddit 讨论 - 在 Aider 中使用 OpenRouter 的配置示例](https://www.reddit.com/r/autocoding/comments/1hslsdm/using_openrouter_in_aider/)
- [Aider 官方文档 - 安装指南](https://aider.chat/docs/install.html)
- [OpenRouter 官方文档 - 提供商路由配置](https://openrouter.ai/docs/provider-routing)
- [Aider 官方文档 - 命令使用说明](https://aider.chat/docs/usage/commands.html)
- [Aider 官方文档 - 模型警告和元数据配置](https://aider.chat/docs/llms/warnings.html)
- [Aider 官方文档 - 高级模型设置](https://aider.chat/docs/config/adv-model-settings.html)
- [Aider 官方文档 - 常见问题解答](https://aider.chat/docs/faq.html)
- [OpenRouter 官方网站 - 模型和 API 概览](https://openrouter.ai/)

