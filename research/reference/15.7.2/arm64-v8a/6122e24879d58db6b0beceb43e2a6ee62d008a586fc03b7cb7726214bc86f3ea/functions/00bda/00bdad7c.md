# 00bdad7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae3c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae3c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0045.md#compare-521b96dd89b3eef39588a074f6906a2c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdad7c",
  "name": "FUN_00bdad7c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e353ee10cb7a17912b1875ebfb49292d45e8ea77707ffc03e733f53a04fb8d8d",
  "source_text_sha256": "e353ee10cb7a17912b1875ebfb49292d45e8ea77707ffc03e733f53a04fb8d8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdad7c",
        "00bdad83"
      ]
    ],
    "bytes_sha256": "9bc148d8b8efa4992af1171e96dc342d97ef86f67ad2dcbf107629a1cf76b84a",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008d40c0](../008d4/008d40c0.md)

## 呼び出し先

- [008d5008](../008d5/008d5008.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 133 bytes

~~~c

void FUN_00bdad7c(undefined1 param_1 [16])

{
  long in_x9;
  
  FUN_008d5008(param_1,*(undefined8 *)(in_x9 + 0xe10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdad7c"></a> `00bdad7c` | `21 85 c3 3d` | ldr q1,[x9, #0xe10] | `FALL_THROUGH`
<a id="insn-00bdad80"></a> `00bdad80` | `a2 e8 f3 17` | b 0x008d5008 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdad7c`](#insn-00bdad7c) 範囲 `[['00bdad7c', '00bdad83']]`

## 命令位置別の参照

- [`00bdad80`](#insn-00bdad80) → [`008d5008`](../008d5/008d5008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008d5008` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdad80`](#insn-00bdad80)

~~~json
{
  "source": "00bdad80",
  "target": "008d5008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
