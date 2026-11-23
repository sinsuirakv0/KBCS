# 00bdeeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdef60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-116f1fd7fa3282d3ba9c080f9bf97c49)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeeb0",
  "name": "<EXTERNAL>::strcpy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e8bcabc1f496521e68abd31b98fb13a9166f592e346f4fea5b6dd1dbaf76be6",
  "source_text_sha256": "8e8bcabc1f496521e68abd31b98fb13a9166f592e346f4fea5b6dd1dbaf76be6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeeb0",
        "00bdeebf"
      ]
    ],
    "bytes_sha256": "f653e433c33513ee975210abde35d7b3a58072b989fe8d75e70efa203c5e4ca2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b02db4](../00b02/00b02db4.md)

## 呼び出し先

- [010a5608](../010a5/010a5608.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 214 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * strcpy(char *__dest,char *__src)

{
  char *pcVar1;
  
  pcVar1 = (char *)(*(code *)PTR_strcpy_00c1df90)();
  return pcVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeeb0"></a> `00bdeeb0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeeb4"></a> `00bdeeb4` | `11 ca 47 f9` | ldr x17,[x16, #0xf90] | `FALL_THROUGH`
<a id="insn-00bdeeb8"></a> `00bdeeb8` | `10 42 3e 91` | add x16,x16,#0xf90 | `FALL_THROUGH`
<a id="insn-00bdeebc"></a> `00bdeebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeeb0`](#insn-00bdeeb0) 範囲 `[['00bdeeb0', '00bdeebf']]`

## 命令位置別の参照

- [`00bdeeb4`](#insn-00bdeeb4) → `00c1df90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeebc`](#insn-00bdeebc) → [`010a5608`](../010a5/010a5608.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5608` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeeb4`](#insn-00bdeeb4)

~~~json
{
  "source": "00bdeeb4",
  "target": "00c1df90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeebc`](#insn-00bdeebc)

~~~json
{
  "source": "00bdeebc",
  "target": "010a5608",
  "target_space": "ram",
  "resolution": "function"
}
~~~
