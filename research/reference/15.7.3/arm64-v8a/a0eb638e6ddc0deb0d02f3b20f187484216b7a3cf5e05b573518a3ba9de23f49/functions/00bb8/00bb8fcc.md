# 00bb8fcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bb8f04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8f04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3e990d60754454ff50bc9be701849f05)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bb9010`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9010.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-0eb088eda627dc0683b3298ed3ae16ab)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8fcc",
  "name": "FUN_00bb8fcc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d8ef82eb0ff2e8d131bc534fc37630aaf7c5c0dc3a1c4e1ad3c1ec9844505d4",
  "source_text_sha256": "2d8ef82eb0ff2e8d131bc534fc37630aaf7c5c0dc3a1c4e1ad3c1ec9844505d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8fcc",
        "00bb901b"
      ]
    ],
    "bytes_sha256": "959a15ec37f6c0609417b59b1e62c3a8110869b54ea6cdca412bdd5cc5dcb8f3",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 253 bytes

~~~c

void FUN_00bb8fcc(void)

{
  long lVar1;
  
  lVar1 = 0x240;
  do {
    if ((*(byte *)((long)&DAT_010a2ef4 + lVar1 + 4) & 1) != 0) {
      _ZdlPv(*(void **)(&DAT_010a2f08 + lVar1));
    }
    lVar1 = lVar1 + -0x18;
  } while (lVar1 != 0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb8fcc"></a> `00bb8fcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb8fd0"></a> `00bb8fd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb8fd4"></a> `00bb8fd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8fd8"></a> `00bb8fd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb8fdc"></a> `00bb8fdc` | `13 48 80 52` | mov w19,#0x240 | `FALL_THROUGH`
<a id="insn-00bb8fe0"></a> `00bb8fe0` | `54 27 00 d0` | adrp x20,0x10a2000 | `FALL_THROUGH`
<a id="insn-00bb8fe4"></a> `00bb8fe4` | `94 42 3c 91` | add x20,x20,#0xf10 | `FALL_THROUGH`
<a id="insn-00bb8fe8"></a> `00bb8fe8` | `03 00 00 14` | b 0x00bb8ff4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb8fec"></a> `00bb8fec` | `73 62 00 f1` | subs x19,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bb8ff0"></a> `00bb8ff0` | `e0 00 00 54` | b.eq 0x00bb900c | `CONDITIONAL_JUMP`
<a id="insn-00bb8ff4"></a> `00bb8ff4` | `88 02 13 8b` | add x8,x20,x19 | `FALL_THROUGH`
<a id="insn-00bb8ff8"></a> `00bb8ff8` | `09 81 5e 38` | ldurb w9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bb8ffc"></a> `00bb8ffc` | `89 ff 07 36` | tbz w9,#0x0,0x00bb8fec | `CONDITIONAL_JUMP`
<a id="insn-00bb9000"></a> `00bb9000` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bb9004"></a> `00bb9004` | `03 88 00 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00bb9008"></a> `00bb9008` | `f9 ff ff 17` | b 0x00bb8fec | `UNCONDITIONAL_JUMP`
<a id="insn-00bb900c"></a> `00bb900c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb9010"></a> `00bb9010` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb9014"></a> `00bb9014` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb9018"></a> `00bb9018` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8fcc`](#insn-00bb8fcc) 範囲 `[['00bb8fcc', '00bb8feb']]`
  - `UNCONDITIONAL_JUMP` [`00bb8fe8`](#insn-00bb8fe8) → [`00bb8ff4`](#insn-00bb8ff4)
- ブロック [`00bb8fec`](#insn-00bb8fec) 範囲 `[['00bb8fec', '00bb8ff3']]`
  - `CONDITIONAL_JUMP` [`00bb8ff0`](#insn-00bb8ff0) → [`00bb900c`](#insn-00bb900c)
  - `FALL_THROUGH` [`00bb8ff0`](#insn-00bb8ff0) → [`00bb8ff4`](#insn-00bb8ff4)
- ブロック [`00bb8ff4`](#insn-00bb8ff4) 範囲 `[['00bb8ff4', '00bb8fff']]`
  - `CONDITIONAL_JUMP` [`00bb8ffc`](#insn-00bb8ffc) → [`00bb8fec`](#insn-00bb8fec)
  - `FALL_THROUGH` [`00bb8ffc`](#insn-00bb8ffc) → [`00bb9000`](#insn-00bb9000)
- ブロック [`00bb9000`](#insn-00bb9000) 範囲 `[['00bb9000', '00bb900b']]`
  - `UNCONDITIONAL_JUMP` [`00bb9008`](#insn-00bb9008) → [`00bb8fec`](#insn-00bb8fec)
- ブロック [`00bb900c`](#insn-00bb900c) 範囲 `[['00bb900c', '00bb901b']]`

## 命令位置別の参照

- [`00bb8fd0`](#insn-00bb8fd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8fd4`](#insn-00bb8fd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8fe8`](#insn-00bb8fe8) → [`00bb8ff4`](#insn-00bb8ff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8ff0`](#insn-00bb8ff0) → [`00bb900c`](#insn-00bb900c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8ff8`](#insn-00bb8ff8) → `010a3138`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8ff8`](#insn-00bb8ff8) → `010a3120`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8ff8`](#insn-00bb8ff8) → `010a3108`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bb8ffc`](#insn-00bb8ffc) → [`00bb8fec`](#insn-00bb8fec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9000`](#insn-00bb9000) → `010a3148`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9000`](#insn-00bb9000) → `010a3130`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9000`](#insn-00bb9000) → `010a3118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb9004`](#insn-00bb9004) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00bb9008`](#insn-00bb9008) → [`00bb8fec`](#insn-00bb8fec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb900c`](#insn-00bb900c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb9010`](#insn-00bb9010) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8fd0`](#insn-00bb8fd0)

~~~json
{
  "source": "00bb8fd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8fd4`](#insn-00bb8fd4)

~~~json
{
  "source": "00bb8fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8fe8`](#insn-00bb8fe8)

~~~json
{
  "source": "00bb8fe8",
  "target": "00bb8ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8ff0`](#insn-00bb8ff0)

~~~json
{
  "source": "00bb8ff0",
  "target": "00bb900c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8ff8`](#insn-00bb8ff8)

~~~json
{
  "source": "00bb8ff8",
  "target": "010a3138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3138",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8ff8`](#insn-00bb8ff8)

~~~json
{
  "source": "00bb8ff8",
  "target": "010a3120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3120",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8ff8`](#insn-00bb8ff8)

~~~json
{
  "source": "00bb8ff8",
  "target": "010a3108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3108",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8ffc`](#insn-00bb8ffc)

~~~json
{
  "source": "00bb8ffc",
  "target": "00bb8fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9000`](#insn-00bb9000)

~~~json
{
  "source": "00bb9000",
  "target": "010a3148",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3148",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9000`](#insn-00bb9000)

~~~json
{
  "source": "00bb9000",
  "target": "010a3130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9000`](#insn-00bb9000)

~~~json
{
  "source": "00bb9000",
  "target": "010a3118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3118",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb9004`](#insn-00bb9004)

~~~json
{
  "source": "00bb9004",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb9008`](#insn-00bb9008)

~~~json
{
  "source": "00bb9008",
  "target": "00bb8fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb900c`](#insn-00bb900c)

~~~json
{
  "source": "00bb900c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb9010`](#insn-00bb9010)

~~~json
{
  "source": "00bb9010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
