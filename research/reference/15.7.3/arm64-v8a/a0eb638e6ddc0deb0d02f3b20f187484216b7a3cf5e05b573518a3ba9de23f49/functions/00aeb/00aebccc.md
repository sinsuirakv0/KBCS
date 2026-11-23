# 00aebccc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebc04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebc04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-e203611d71bba29413bfbd27815dba25)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebd10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-a59c996bbb302876fc38ae21d636b7b0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebccc",
  "name": "_ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e719b4cd04c57461a9760ba51773225c6baba5d8b9424eed28d3d56992f464a",
  "source_text_sha256": "3e719b4cd04c57461a9760ba51773225c6baba5d8b9424eed28d3d56992f464a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebccc",
        "00aebd6b"
      ]
    ],
    "bytes_sha256": "abc7ca646aa89c5ef96e69c07948a0b488285eaf834e232484c3ccadbd4fd497",
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

## 疑似コード / UTF-8 508 bytes

~~~c

void _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a08b8 != 0) {
    if (DAT_010a08c0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a08c0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a08b8);
    DAT_010a08b8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebccc"></a> `00aebccc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aebcd0"></a> `00aebcd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebcd4"></a> `00aebcd4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebcd8"></a> `00aebcd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aebcdc"></a> `00aebcdc` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebce0"></a> `00aebce0` | `81 5e 44 f9` | ldr x1,[x20, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebce4"></a> `00aebce4` | `c1 03 00 b4` | cbz x1,0x00aebd5c | `CONDITIONAL_JUMP`
<a id="insn-00aebce8"></a> `00aebce8` | `b5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebcec"></a> `00aebcec` | `a8 02 63 39` | ldrb w8,[x21, #0x8c0] | `FALL_THROUGH`
<a id="insn-00aebcf0"></a> `00aebcf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebcf4"></a> `00aebcf4` | `c8 00 00 34` | cbz w8,0x00aebd0c | `CONDITIONAL_JUMP`
<a id="insn-00aebcf8"></a> `00aebcf8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebcfc"></a> `00aebcfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd00"></a> `00aebd00` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aebd04"></a> `00aebd04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebd08"></a> `00aebd08` | `bf 02 23 39` | strb wzr,[x21, #0x8c0] | `FALL_THROUGH`
<a id="insn-00aebd0c"></a> `00aebd0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebd10"></a> `00aebd10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd14"></a> `00aebd14` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aebd18"></a> `00aebd18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebd1c"></a> `00aebd1c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aebd20"></a> `00aebd20` | `20 01 00 54` | b.eq 0x00aebd44 | `CONDITIONAL_JUMP`
<a id="insn-00aebd24"></a> `00aebd24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebd28"></a> `00aebd28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd2c"></a> `00aebd2c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aebd30"></a> `00aebd30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebd34"></a> `00aebd34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebd38"></a> `00aebd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd3c"></a> `00aebd3c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aebd40"></a> `00aebd40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebd44"></a> `00aebd44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebd48"></a> `00aebd48` | `81 5e 44 f9` | ldr x1,[x20, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebd4c"></a> `00aebd4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd50"></a> `00aebd50` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aebd54"></a> `00aebd54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aebd58"></a> `00aebd58` | `9f 5e 04 f9` | str xzr,[x20, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebd5c"></a> `00aebd5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebd60"></a> `00aebd60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebd64"></a> `00aebd64` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aebd68"></a> `00aebd68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebccc`](#insn-00aebccc) 範囲 `[['00aebccc', '00aebce7']]`
  - `CONDITIONAL_JUMP` [`00aebce4`](#insn-00aebce4) → [`00aebd5c`](#insn-00aebd5c)
  - `FALL_THROUGH` [`00aebce4`](#insn-00aebce4) → [`00aebce8`](#insn-00aebce8)
- ブロック [`00aebce8`](#insn-00aebce8) 範囲 `[['00aebce8', '00aebcf7']]`
  - `CONDITIONAL_JUMP` [`00aebcf4`](#insn-00aebcf4) → [`00aebd0c`](#insn-00aebd0c)
  - `FALL_THROUGH` [`00aebcf4`](#insn-00aebcf4) → [`00aebcf8`](#insn-00aebcf8)
- ブロック [`00aebcf8`](#insn-00aebcf8) 範囲 `[['00aebcf8', '00aebd0b']]`
  - `FALL_THROUGH` [`00aebd08`](#insn-00aebd08) → [`00aebd0c`](#insn-00aebd0c)
- ブロック [`00aebd0c`](#insn-00aebd0c) 範囲 `[['00aebd0c', '00aebd23']]`
  - `CONDITIONAL_JUMP` [`00aebd20`](#insn-00aebd20) → [`00aebd44`](#insn-00aebd44)
  - `FALL_THROUGH` [`00aebd20`](#insn-00aebd20) → [`00aebd24`](#insn-00aebd24)
- ブロック [`00aebd24`](#insn-00aebd24) 範囲 `[['00aebd24', '00aebd43']]`
  - `FALL_THROUGH` [`00aebd40`](#insn-00aebd40) → [`00aebd44`](#insn-00aebd44)
- ブロック [`00aebd44`](#insn-00aebd44) 範囲 `[['00aebd44', '00aebd5b']]`
  - `FALL_THROUGH` [`00aebd58`](#insn-00aebd58) → [`00aebd5c`](#insn-00aebd5c)
- ブロック [`00aebd5c`](#insn-00aebd5c) 範囲 `[['00aebd5c', '00aebd6b']]`

## 命令位置別の参照

- [`00aebccc`](#insn-00aebccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcd0`](#insn-00aebcd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcd4`](#insn-00aebcd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebce0`](#insn-00aebce0) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebce4`](#insn-00aebce4) → [`00aebd5c`](#insn-00aebd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcec`](#insn-00aebcec) → `010a08c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aebcf4`](#insn-00aebcf4) → [`00aebd0c`](#insn-00aebd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd08`](#insn-00aebd08) → `010a08c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aebd20`](#insn-00aebd20) → [`00aebd44`](#insn-00aebd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd48`](#insn-00aebd48) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebd58`](#insn-00aebd58) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebd5c`](#insn-00aebd5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebd60`](#insn-00aebd60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebccc`](#insn-00aebccc)

~~~json
{
  "source": "00aebccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcd0`](#insn-00aebcd0)

~~~json
{
  "source": "00aebcd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcd4`](#insn-00aebcd4)

~~~json
{
  "source": "00aebcd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebce0`](#insn-00aebce0)

~~~json
{
  "source": "00aebce0",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebce4`](#insn-00aebce4)

~~~json
{
  "source": "00aebce4",
  "target": "00aebd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcec`](#insn-00aebcec)

~~~json
{
  "source": "00aebcec",
  "target": "010a08c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebcf4`](#insn-00aebcf4)

~~~json
{
  "source": "00aebcf4",
  "target": "00aebd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd08`](#insn-00aebd08)

~~~json
{
  "source": "00aebd08",
  "target": "010a08c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebd20`](#insn-00aebd20)

~~~json
{
  "source": "00aebd20",
  "target": "00aebd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd48`](#insn-00aebd48)

~~~json
{
  "source": "00aebd48",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebd58`](#insn-00aebd58)

~~~json
{
  "source": "00aebd58",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebd5c`](#insn-00aebd5c)

~~~json
{
  "source": "00aebd5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebd60`](#insn-00aebd60)

~~~json
{
  "source": "00aebd60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
