# 00aecb6c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aecaa4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-867e5a7d332169d81777c5b5e54f23c3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aecbb0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-39153b1612947b4d10444c2287c1458c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecb6c",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72a9e0fa9b22e30594f1a9fdc2389fc93894842f29e4e057bc7c98a0285e7600",
  "source_text_sha256": "72a9e0fa9b22e30594f1a9fdc2389fc93894842f29e4e057bc7c98a0285e7600",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecb6c",
        "00aecc0b"
      ]
    ],
    "bytes_sha256": "07fc932d85c1a4a527a0e1eb003a0f2906a0526843eb75edc395a72e3680c461",
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

## 疑似コード / UTF-8 620 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
                    /* try { // try from 00aecb70 to 00becb7f has its CatchHandler @ 00af1a40 */
  if (DAT_010a0968 != 0) {
    if (DAT_010a0970 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0970 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0968);
    DAT_010a0968 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecb6c"></a> `00aecb6c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecb70"></a> `00aecb70` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecb74"></a> `00aecb74` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecb78"></a> `00aecb78` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecb7c"></a> `00aecb7c` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecb80"></a> `00aecb80` | `81 b6 44 f9` | ldr x1,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aecb84"></a> `00aecb84` | `c1 03 00 b4` | cbz x1,0x00aecbfc | `CONDITIONAL_JUMP`
<a id="insn-00aecb88"></a> `00aecb88` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecb8c"></a> `00aecb8c` | `a8 c2 65 39` | ldrb w8,[x21, #0x970] | `FALL_THROUGH`
<a id="insn-00aecb90"></a> `00aecb90` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecb94"></a> `00aecb94` | `c8 00 00 34` | cbz w8,0x00aecbac | `CONDITIONAL_JUMP`
<a id="insn-00aecb98"></a> `00aecb98` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb9c"></a> `00aecb9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecba0"></a> `00aecba0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aecba4"></a> `00aecba4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecba8"></a> `00aecba8` | `bf c2 25 39` | strb wzr,[x21, #0x970] | `FALL_THROUGH`
<a id="insn-00aecbac"></a> `00aecbac` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbb0"></a> `00aecbb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbb4"></a> `00aecbb4` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aecbb8"></a> `00aecbb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecbbc"></a> `00aecbbc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecbc0"></a> `00aecbc0` | `20 01 00 54` | b.eq 0x00aecbe4 | `CONDITIONAL_JUMP`
<a id="insn-00aecbc4"></a> `00aecbc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbc8"></a> `00aecbc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbcc"></a> `00aecbcc` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aecbd0"></a> `00aecbd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecbd4"></a> `00aecbd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbd8"></a> `00aecbd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbdc"></a> `00aecbdc` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecbe0"></a> `00aecbe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecbe4"></a> `00aecbe4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbe8"></a> `00aecbe8` | `81 b6 44 f9` | ldr x1,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aecbec"></a> `00aecbec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbf0"></a> `00aecbf0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aecbf4"></a> `00aecbf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecbf8"></a> `00aecbf8` | `9f b6 04 f9` | str xzr,[x20, #0x968] | `FALL_THROUGH`
<a id="insn-00aecbfc"></a> `00aecbfc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecc00"></a> `00aecc00` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc04"></a> `00aecc04` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecc08"></a> `00aecc08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecb6c`](#insn-00aecb6c) 範囲 `[['00aecb6c', '00aecb6f']]`
  - `FALL_THROUGH` [`00aecb6c`](#insn-00aecb6c) → [`00aecb70`](#insn-00aecb70)
- ブロック [`00aecb70`](#insn-00aecb70) 範囲 `[['00aecb70', '00aecb87']]`
  - `CONDITIONAL_JUMP` [`00aecb84`](#insn-00aecb84) → [`00aecbfc`](#insn-00aecbfc)
  - `FALL_THROUGH` [`00aecb84`](#insn-00aecb84) → [`00aecb88`](#insn-00aecb88)
- ブロック [`00aecb88`](#insn-00aecb88) 範囲 `[['00aecb88', '00aecb97']]`
  - `CONDITIONAL_JUMP` [`00aecb94`](#insn-00aecb94) → [`00aecbac`](#insn-00aecbac)
  - `FALL_THROUGH` [`00aecb94`](#insn-00aecb94) → [`00aecb98`](#insn-00aecb98)
- ブロック [`00aecb98`](#insn-00aecb98) 範囲 `[['00aecb98', '00aecbab']]`
  - `FALL_THROUGH` [`00aecba8`](#insn-00aecba8) → [`00aecbac`](#insn-00aecbac)
- ブロック [`00aecbac`](#insn-00aecbac) 範囲 `[['00aecbac', '00aecbc3']]`
  - `CONDITIONAL_JUMP` [`00aecbc0`](#insn-00aecbc0) → [`00aecbe4`](#insn-00aecbe4)
  - `FALL_THROUGH` [`00aecbc0`](#insn-00aecbc0) → [`00aecbc4`](#insn-00aecbc4)
- ブロック [`00aecbc4`](#insn-00aecbc4) 範囲 `[['00aecbc4', '00aecbe3']]`
  - `FALL_THROUGH` [`00aecbe0`](#insn-00aecbe0) → [`00aecbe4`](#insn-00aecbe4)
- ブロック [`00aecbe4`](#insn-00aecbe4) 範囲 `[['00aecbe4', '00aecbfb']]`
  - `FALL_THROUGH` [`00aecbf8`](#insn-00aecbf8) → [`00aecbfc`](#insn-00aecbfc)
- ブロック [`00aecbfc`](#insn-00aecbfc) 範囲 `[['00aecbfc', '00aecc0b']]`

## 命令位置別の参照

- [`00aecb6c`](#insn-00aecb6c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb70`](#insn-00aecb70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb74`](#insn-00aecb74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb80`](#insn-00aecb80) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecb84`](#insn-00aecb84) → [`00aecbfc`](#insn-00aecbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb8c`](#insn-00aecb8c) → `010a0970`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecb94`](#insn-00aecb94) → [`00aecbac`](#insn-00aecbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecba8`](#insn-00aecba8) → `010a0970`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecbc0`](#insn-00aecbc0) → [`00aecbe4`](#insn-00aecbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbe8`](#insn-00aecbe8) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecbf8`](#insn-00aecbf8) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecbfc`](#insn-00aecbfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc00`](#insn-00aecc00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecb6c`](#insn-00aecb6c)

~~~json
{
  "source": "00aecb6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb70`](#insn-00aecb70)

~~~json
{
  "source": "00aecb70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb74`](#insn-00aecb74)

~~~json
{
  "source": "00aecb74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb80`](#insn-00aecb80)

~~~json
{
  "source": "00aecb80",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecb84`](#insn-00aecb84)

~~~json
{
  "source": "00aecb84",
  "target": "00aecbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb8c`](#insn-00aecb8c)

~~~json
{
  "source": "00aecb8c",
  "target": "010a0970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0970",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecb94`](#insn-00aecb94)

~~~json
{
  "source": "00aecb94",
  "target": "00aecbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecba8`](#insn-00aecba8)

~~~json
{
  "source": "00aecba8",
  "target": "010a0970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0970",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecbc0`](#insn-00aecbc0)

~~~json
{
  "source": "00aecbc0",
  "target": "00aecbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbe8`](#insn-00aecbe8)

~~~json
{
  "source": "00aecbe8",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecbf8`](#insn-00aecbf8)

~~~json
{
  "source": "00aecbf8",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecbfc`](#insn-00aecbfc)

~~~json
{
  "source": "00aecbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc00`](#insn-00aecc00)

~~~json
{
  "source": "00aecc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
