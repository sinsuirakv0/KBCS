# 00baef1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baefe4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefe4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-14d07852d06e763fa0478f0bbe72669d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baef1c",
  "name": "_ZNSt6__ndk18numpunctIwEC2Em",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "011ac845cff15c6a87662bd3df46817877a99719792cb98f6a4912b46bd5ce03",
  "source_text_sha256": "011ac845cff15c6a87662bd3df46817877a99719792cb98f6a4912b46bd5ce03",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baef1c",
        "00baef4b"
      ]
    ],
    "bytes_sha256": "48e6ffcf90ef200b0d10a41e5dd4655adfbd31cda285444d88fdbaf94487fa8f",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1720](../00be1/00be1720.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk18numpunctIwEC2Em(long *param_1,long param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bec0;
  lVar1 = DAT_002b2b98;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  param_1[2] = lVar1;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baef1c"></a> `00baef1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baef20"></a> `00baef20` | `69 03 00 b0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00baef24"></a> `00baef24` | `28 b8 ff 90` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00baef28"></a> `00baef28` | `2a 04 00 d1` | sub x10,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00baef2c"></a> `00baef2c` | `29 61 47 f9` | ldr x9,[x9, #0xec0] | `FALL_THROUGH`
<a id="insn-00baef30"></a> `00baef30` | `00 cd 45 fd` | ldr d0,[x8, #0xb98] | `FALL_THROUGH`
<a id="insn-00baef34"></a> `00baef34` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baef38"></a> `00baef38` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baef3c"></a> `00baef3c` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00baef40"></a> `00baef40` | `00 08 00 fd` | str d0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baef44"></a> `00baef44` | `08 28 00 a9` | stp x8,x10,[x0] | `FALL_THROUGH`
<a id="insn-00baef48"></a> `00baef48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baef1c`](#insn-00baef1c) 範囲 `[['00baef1c', '00baef4b']]`

## 命令位置別の参照

- [`00baef2c`](#insn-00baef2c) → `00c1bec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baef30`](#insn-00baef30) → `002b2b98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00baef44`](#insn-00baef44) → `00c13ac8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baef2c`](#insn-00baef2c)

~~~json
{
  "source": "00baef2c",
  "target": "00c1bec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bec0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baef30`](#insn-00baef30)

~~~json
{
  "source": "00baef30",
  "target": "002b2b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "2e0000002c000000",
  "capture_start": "002b2b98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baef44`](#insn-00baef44)

~~~json
{
  "source": "00baef44",
  "target": "00c13ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13ab8",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
