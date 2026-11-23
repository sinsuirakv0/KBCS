# 00aecad0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeca08`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-5074f7ca632e49ccfa06412caab05882)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aecb14`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-285d8f0a51d8557ad369cb840569bf4d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecad0",
  "name": "_ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "73665d9f2dad8812cab32847fed062d9b55e15eade033ab459cba93ae390ab68",
  "source_text_sha256": "73665d9f2dad8812cab32847fed062d9b55e15eade033ab459cba93ae390ab68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecad0",
        "00aecb6b"
      ]
    ],
    "bytes_sha256": "58bc576000fd3ffaf25eea3d22e065e9d66c396a499f77529f1a58d4c00acb73",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 718 bytes

~~~c

bool _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
                    /* try { // try from 00aecae8 to 00becaef has its CatchHandler @ 00af1a38 */
  if (DAT_010a0970 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0968,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0970 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0970;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecad0"></a> `00aecad0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecad4"></a> `00aecad4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecad8"></a> `00aecad8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecadc"></a> `00aecadc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecae0"></a> `00aecae0` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecae4"></a> `00aecae4` | `a8 c2 65 39` | ldrb w8,[x21, #0x970] | `FALL_THROUGH`
<a id="insn-00aecae8"></a> `00aecae8` | `68 00 00 34` | cbz w8,0x00aecaf4 | `CONDITIONAL_JUMP`
<a id="insn-00aecaec"></a> `00aecaec` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aecaf0"></a> `00aecaf0` | `1b 00 00 14` | b 0x00aecb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00aecaf4"></a> `00aecaf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aecaf8"></a> `00aecaf8` | `a9 2d 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecafc"></a> `00aecafc` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aecb00"></a> `00aecb00` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aecb04"></a> `00aecb04` | `21 b5 44 f9` | ldr x1,[x9, #0x968] | `FALL_THROUGH`
<a id="insn-00aecb08"></a> `00aecb08` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aecb0c"></a> `00aecb0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecb10"></a> `00aecb10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb14"></a> `00aecb14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb18"></a> `00aecb18` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aecb1c"></a> `00aecb1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb20"></a> `00aecb20` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aecb24"></a> `00aecb24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb28"></a> `00aecb28` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecb2c"></a> `00aecb2c` | `20 01 00 54` | b.eq 0x00aecb50 | `CONDITIONAL_JUMP`
<a id="insn-00aecb30"></a> `00aecb30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb34"></a> `00aecb34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb38"></a> `00aecb38` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aecb3c"></a> `00aecb3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb40"></a> `00aecb40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb44"></a> `00aecb44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb48"></a> `00aecb48` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecb4c"></a> `00aecb4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb50"></a> `00aecb50` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aecb54"></a> `00aecb54` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aecb58"></a> `00aecb58` | `a0 c2 25 39` | strb w0,[x21, #0x970] | `FALL_THROUGH`
<a id="insn-00aecb5c"></a> `00aecb5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecb60"></a> `00aecb60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecb64"></a> `00aecb64` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecb68"></a> `00aecb68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecad0`](#insn-00aecad0) 範囲 `[['00aecad0', '00aecae7']]`
  - `FALL_THROUGH` [`00aecae4`](#insn-00aecae4) → [`00aecae8`](#insn-00aecae8)
- ブロック [`00aecae8`](#insn-00aecae8) 範囲 `[['00aecae8', '00aecaeb']]`
  - `CONDITIONAL_JUMP` [`00aecae8`](#insn-00aecae8) → [`00aecaf4`](#insn-00aecaf4)
  - `FALL_THROUGH` [`00aecae8`](#insn-00aecae8) → [`00aecaec`](#insn-00aecaec)
- ブロック [`00aecaec`](#insn-00aecaec) 範囲 `[['00aecaec', '00aecaf3']]`
  - `UNCONDITIONAL_JUMP` [`00aecaf0`](#insn-00aecaf0) → [`00aecb5c`](#insn-00aecb5c)
- ブロック [`00aecaf4`](#insn-00aecaf4) 範囲 `[['00aecaf4', '00aecb2f']]`
  - `CONDITIONAL_JUMP` [`00aecb2c`](#insn-00aecb2c) → [`00aecb50`](#insn-00aecb50)
  - `FALL_THROUGH` [`00aecb2c`](#insn-00aecb2c) → [`00aecb30`](#insn-00aecb30)
- ブロック [`00aecb30`](#insn-00aecb30) 範囲 `[['00aecb30', '00aecb4f']]`
  - `FALL_THROUGH` [`00aecb4c`](#insn-00aecb4c) → [`00aecb50`](#insn-00aecb50)
- ブロック [`00aecb50`](#insn-00aecb50) 範囲 `[['00aecb50', '00aecb5b']]`
  - `FALL_THROUGH` [`00aecb58`](#insn-00aecb58) → [`00aecb5c`](#insn-00aecb5c)
- ブロック [`00aecb5c`](#insn-00aecb5c) 範囲 `[['00aecb5c', '00aecb6b']]`

## 命令位置別の参照

- [`00aecad0`](#insn-00aecad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecad4`](#insn-00aecad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecad8`](#insn-00aecad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecae4`](#insn-00aecae4) → `010a0970`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecae8`](#insn-00aecae8) → [`00aecaf4`](#insn-00aecaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecaf0`](#insn-00aecaf0) → [`00aecb5c`](#insn-00aecb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb04`](#insn-00aecb04) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecb2c`](#insn-00aecb2c) → [`00aecb50`](#insn-00aecb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb58`](#insn-00aecb58) → `010a0970`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecb5c`](#insn-00aecb5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb60`](#insn-00aecb60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecad0`](#insn-00aecad0)

~~~json
{
  "source": "00aecad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecad4`](#insn-00aecad4)

~~~json
{
  "source": "00aecad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecad8`](#insn-00aecad8)

~~~json
{
  "source": "00aecad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecae4`](#insn-00aecae4)

~~~json
{
  "source": "00aecae4",
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
- 参照命令 [`00aecae8`](#insn-00aecae8)

~~~json
{
  "source": "00aecae8",
  "target": "00aecaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecaf0`](#insn-00aecaf0)

~~~json
{
  "source": "00aecaf0",
  "target": "00aecb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb04`](#insn-00aecb04)

~~~json
{
  "source": "00aecb04",
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
- 参照命令 [`00aecb2c`](#insn-00aecb2c)

~~~json
{
  "source": "00aecb2c",
  "target": "00aecb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb58`](#insn-00aecb58)

~~~json
{
  "source": "00aecb58",
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
- 参照命令 [`00aecb5c`](#insn-00aecb5c)

~~~json
{
  "source": "00aecb5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb60`](#insn-00aecb60)

~~~json
{
  "source": "00aecb60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
