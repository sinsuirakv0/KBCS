# 00aacc1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aacce4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacce4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0055.md#compare-27c6bfe84a87915662fff5ca23b99979)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aacc1c",
  "name": "FUN_00aacc1c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b9811b362e0a669ad3e5120db3a504507ad337de59d147877abc120ff09c63c",
  "source_text_sha256": "6b9811b362e0a669ad3e5120db3a504507ad337de59d147877abc120ff09c63c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aacc1c",
        "00aacc5b"
      ]
    ],
    "bytes_sha256": "de622f0df1b1ffd18e6300dcc703f1f496db8aedfd3f6581694bfa035f939783",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_00aacc1c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x20);
  uVar4 = *(undefined8 *)(param_1 + 0x10);
  uVar3 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined8 *)(param_1 + 0x18);
  *puVar1 = &PTR_FUN_00c0f1d8;
  puVar1[2] = uVar4;
  puVar1[1] = uVar3;
  puVar1[3] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aacc1c"></a> `00aacc1c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aacc20"></a> `00aacc20` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aacc24"></a> `00aacc24` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aacc28"></a> `00aacc28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aacc2c"></a> `00aacc2c` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00aacc30"></a> `00aacc30` | `c4 b8 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aacc34"></a> `00aacc34` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aacc38"></a> `00aacc38` | `69 0e 40 f9` | ldr x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aacc3c"></a> `00aacc3c` | `08 0b 00 f0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aacc40"></a> `00aacc40` | `08 61 07 91` | add x8,x8,#0x1d8 | `FALL_THROUGH`
<a id="insn-00aacc44"></a> `00aacc44` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aacc48"></a> `00aacc48` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aacc4c"></a> `00aacc4c` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00aacc50"></a> `00aacc50` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aacc54"></a> `00aacc54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aacc58"></a> `00aacc58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aacc1c`](#insn-00aacc1c) 範囲 `[['00aacc1c', '00aacc5b']]`

## 命令位置別の参照

- [`00aacc1c`](#insn-00aacc1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc20`](#insn-00aacc20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc30`](#insn-00aacc30) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aacc44`](#insn-00aacc44) → `00c0f1d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aacc50`](#insn-00aacc50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc54`](#insn-00aacc54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aacc1c`](#insn-00aacc1c)

~~~json
{
  "source": "00aacc1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc20`](#insn-00aacc20)

~~~json
{
  "source": "00aacc20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc30`](#insn-00aacc30)

~~~json
{
  "source": "00aacc30",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacc44`](#insn-00aacc44)

~~~json
{
  "source": "00aacc44",
  "target": "00c0f1d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f1d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacc50`](#insn-00aacc50)

~~~json
{
  "source": "00aacc50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc54`](#insn-00aacc54)

~~~json
{
  "source": "00aacc54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
