# 00b4ccdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aecf58`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecf58.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-8008af6fbddf34d069bf9ce540a729cb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4d104`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0073.md#compare-9447406cce23c9a79765f0724a24e446)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4ccdc",
  "name": "_ZN8firebase4util3set12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3de4ad409c290766ef6e04631c561aecb02bd6c32c911dcab8eb84b10a5e86b",
  "source_text_sha256": "c3de4ad409c290766ef6e04631c561aecb02bd6c32c911dcab8eb84b10a5e86b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4ccdc",
        "00b4cd7b"
      ]
    ],
    "bytes_sha256": "d67fc3fb7ddcb66e29d6dd47922002874840fda6705daf8ff45c1d40edd60fe5",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01125888 != 0) {
    if (DAT_01125890 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01125890 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01125888);
    DAT_01125888 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4ccdc"></a> `00b4ccdc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4cce0"></a> `00b4cce0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cce4"></a> `00b4cce4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4cce8"></a> `00b4cce8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4ccec"></a> `00b4ccec` | `d4 2e 00 b0` | adrp x20,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4ccf0"></a> `00b4ccf0` | `81 46 44 f9` | ldr x1,[x20, #0x888] | `FALL_THROUGH`
<a id="insn-00b4ccf4"></a> `00b4ccf4` | `c1 03 00 b4` | cbz x1,0x00b4cd6c | `CONDITIONAL_JUMP`
<a id="insn-00b4ccf8"></a> `00b4ccf8` | `d5 2e 00 b0` | adrp x21,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4ccfc"></a> `00b4ccfc` | `a8 42 62 39` | ldrb w8,[x21, #0x890] | `FALL_THROUGH`
<a id="insn-00b4cd00"></a> `00b4cd00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4cd04"></a> `00b4cd04` | `c8 00 00 34` | cbz w8,0x00b4cd1c | `CONDITIONAL_JUMP`
<a id="insn-00b4cd08"></a> `00b4cd08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4cd0c"></a> `00b4cd0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4cd10"></a> `00b4cd10` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b4cd14"></a> `00b4cd14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4cd18"></a> `00b4cd18` | `bf 42 22 39` | strb wzr,[x21, #0x890] | `FALL_THROUGH`
<a id="insn-00b4cd1c"></a> `00b4cd1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4cd20"></a> `00b4cd20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4cd24"></a> `00b4cd24` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4cd28"></a> `00b4cd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4cd2c"></a> `00b4cd2c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4cd30"></a> `00b4cd30` | `20 01 00 54` | b.eq 0x00b4cd54 | `CONDITIONAL_JUMP`
<a id="insn-00b4cd34"></a> `00b4cd34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4cd38"></a> `00b4cd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4cd3c"></a> `00b4cd3c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4cd40"></a> `00b4cd40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4cd44"></a> `00b4cd44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4cd48"></a> `00b4cd48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4cd4c"></a> `00b4cd4c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4cd50"></a> `00b4cd50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4cd54"></a> `00b4cd54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4cd58"></a> `00b4cd58` | `81 46 44 f9` | ldr x1,[x20, #0x888] | `FALL_THROUGH`
<a id="insn-00b4cd5c"></a> `00b4cd5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4cd60"></a> `00b4cd60` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4cd64"></a> `00b4cd64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4cd68"></a> `00b4cd68` | `9f 46 04 f9` | str xzr,[x20, #0x888] | `FALL_THROUGH`
<a id="insn-00b4cd6c"></a> `00b4cd6c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4cd70"></a> `00b4cd70` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cd74"></a> `00b4cd74` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4cd78"></a> `00b4cd78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4ccdc`](#insn-00b4ccdc) 範囲 `[['00b4ccdc', '00b4ccf7']]`
  - `CONDITIONAL_JUMP` [`00b4ccf4`](#insn-00b4ccf4) → [`00b4cd6c`](#insn-00b4cd6c)
  - `FALL_THROUGH` [`00b4ccf4`](#insn-00b4ccf4) → [`00b4ccf8`](#insn-00b4ccf8)
- ブロック [`00b4ccf8`](#insn-00b4ccf8) 範囲 `[['00b4ccf8', '00b4cd07']]`
  - `CONDITIONAL_JUMP` [`00b4cd04`](#insn-00b4cd04) → [`00b4cd1c`](#insn-00b4cd1c)
  - `FALL_THROUGH` [`00b4cd04`](#insn-00b4cd04) → [`00b4cd08`](#insn-00b4cd08)
- ブロック [`00b4cd08`](#insn-00b4cd08) 範囲 `[['00b4cd08', '00b4cd1b']]`
  - `FALL_THROUGH` [`00b4cd18`](#insn-00b4cd18) → [`00b4cd1c`](#insn-00b4cd1c)
- ブロック [`00b4cd1c`](#insn-00b4cd1c) 範囲 `[['00b4cd1c', '00b4cd33']]`
  - `CONDITIONAL_JUMP` [`00b4cd30`](#insn-00b4cd30) → [`00b4cd54`](#insn-00b4cd54)
  - `FALL_THROUGH` [`00b4cd30`](#insn-00b4cd30) → [`00b4cd34`](#insn-00b4cd34)
- ブロック [`00b4cd34`](#insn-00b4cd34) 範囲 `[['00b4cd34', '00b4cd53']]`
  - `FALL_THROUGH` [`00b4cd50`](#insn-00b4cd50) → [`00b4cd54`](#insn-00b4cd54)
- ブロック [`00b4cd54`](#insn-00b4cd54) 範囲 `[['00b4cd54', '00b4cd6b']]`
  - `FALL_THROUGH` [`00b4cd68`](#insn-00b4cd68) → [`00b4cd6c`](#insn-00b4cd6c)
- ブロック [`00b4cd6c`](#insn-00b4cd6c) 範囲 `[['00b4cd6c', '00b4cd7b']]`

## 命令位置別の参照

- [`00b4ccdc`](#insn-00b4ccdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cce0`](#insn-00b4cce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cce4`](#insn-00b4cce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccf0`](#insn-00b4ccf0) → `01125888`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ccf4`](#insn-00b4ccf4) → [`00b4cd6c`](#insn-00b4cd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccfc`](#insn-00b4ccfc) → `01125890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4cd04`](#insn-00b4cd04) → [`00b4cd1c`](#insn-00b4cd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd18`](#insn-00b4cd18) → `01125890`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4cd30`](#insn-00b4cd30) → [`00b4cd54`](#insn-00b4cd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd58`](#insn-00b4cd58) → `01125888`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cd68`](#insn-00b4cd68) → `01125888`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cd6c`](#insn-00b4cd6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd70`](#insn-00b4cd70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4ccdc`](#insn-00b4ccdc)

~~~json
{
  "source": "00b4ccdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cce0`](#insn-00b4cce0)

~~~json
{
  "source": "00b4cce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cce4`](#insn-00b4cce4)

~~~json
{
  "source": "00b4cce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccf0`](#insn-00b4ccf0)

~~~json
{
  "source": "00b4ccf0",
  "target": "01125888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125888",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ccf4`](#insn-00b4ccf4)

~~~json
{
  "source": "00b4ccf4",
  "target": "00b4cd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccfc`](#insn-00b4ccfc)

~~~json
{
  "source": "00b4ccfc",
  "target": "01125890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125890",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd04`](#insn-00b4cd04)

~~~json
{
  "source": "00b4cd04",
  "target": "00b4cd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd18`](#insn-00b4cd18)

~~~json
{
  "source": "00b4cd18",
  "target": "01125890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125890",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd30`](#insn-00b4cd30)

~~~json
{
  "source": "00b4cd30",
  "target": "00b4cd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd58`](#insn-00b4cd58)

~~~json
{
  "source": "00b4cd58",
  "target": "01125888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125888",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd68`](#insn-00b4cd68)

~~~json
{
  "source": "00b4cd68",
  "target": "01125888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125888",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd6c`](#insn-00b4cd6c)

~~~json
{
  "source": "00b4cd6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd70`](#insn-00b4cd70)

~~~json
{
  "source": "00b4cd70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
