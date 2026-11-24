# 00aecebc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aece78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-683b938b281012da1a99713b9b9ed155)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4cc40`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-626ae2f262859d3de644a37e9e4d4a8d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecebc",
  "name": "_ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb9ff65685b002cdab8e26cce7fcd5907d475536eeee6efbb95b98d1a69c4b93",
  "source_text_sha256": "cb9ff65685b002cdab8e26cce7fcd5907d475536eeee6efbb95b98d1a69c4b93",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecebc",
        "00aecf57"
      ]
    ],
    "bytes_sha256": "69b4a30deb7789a343d8ebff05ec702f9b19952fcdbd8197150f64cc1985e66c",
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

## 疑似コード / UTF-8 601 bytes

~~~c

bool _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a09d0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a09c8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a09d0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a09d0;
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
<a id="insn-00aecebc"></a> `00aecebc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecec0"></a> `00aecec0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecec4"></a> `00aecec4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecec8"></a> `00aecec8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aececc"></a> `00aececc` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeced0"></a> `00aeced0` | `a8 42 67 39` | ldrb w8,[x21, #0x9d0] | `FALL_THROUGH`
<a id="insn-00aeced4"></a> `00aeced4` | `68 00 00 34` | cbz w8,0x00aecee0 | `CONDITIONAL_JUMP`
<a id="insn-00aeced8"></a> `00aeced8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aecedc"></a> `00aecedc` | `1b 00 00 14` | b 0x00aecf48 | `UNCONDITIONAL_JUMP`
<a id="insn-00aecee0"></a> `00aecee0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aecee4"></a> `00aecee4` | `a9 2d 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecee8"></a> `00aecee8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aeceec"></a> `00aeceec` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aecef0"></a> `00aecef0` | `21 e5 44 f9` | ldr x1,[x9, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aecef4"></a> `00aecef4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aecef8"></a> `00aecef8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecefc"></a> `00aecefc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecf00"></a> `00aecf00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecf04"></a> `00aecf04` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aecf08"></a> `00aecf08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecf0c"></a> `00aecf0c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aecf10"></a> `00aecf10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecf14"></a> `00aecf14` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecf18"></a> `00aecf18` | `20 01 00 54` | b.eq 0x00aecf3c | `CONDITIONAL_JUMP`
<a id="insn-00aecf1c"></a> `00aecf1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecf20"></a> `00aecf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecf24"></a> `00aecf24` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aecf28"></a> `00aecf28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecf2c"></a> `00aecf2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecf30"></a> `00aecf30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecf34"></a> `00aecf34` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecf38"></a> `00aecf38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecf3c"></a> `00aecf3c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aecf40"></a> `00aecf40` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aecf44"></a> `00aecf44` | `a0 42 27 39` | strb w0,[x21, #0x9d0] | `FALL_THROUGH`
<a id="insn-00aecf48"></a> `00aecf48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecf4c"></a> `00aecf4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecf50"></a> `00aecf50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecf54"></a> `00aecf54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecebc`](#insn-00aecebc) 範囲 `[['00aecebc', '00aeced7']]`
  - `CONDITIONAL_JUMP` [`00aeced4`](#insn-00aeced4) → [`00aecee0`](#insn-00aecee0)
  - `FALL_THROUGH` [`00aeced4`](#insn-00aeced4) → [`00aeced8`](#insn-00aeced8)
- ブロック [`00aeced8`](#insn-00aeced8) 範囲 `[['00aeced8', '00aecedf']]`
  - `UNCONDITIONAL_JUMP` [`00aecedc`](#insn-00aecedc) → [`00aecf48`](#insn-00aecf48)
- ブロック [`00aecee0`](#insn-00aecee0) 範囲 `[['00aecee0', '00aecf1b']]`
  - `CONDITIONAL_JUMP` [`00aecf18`](#insn-00aecf18) → [`00aecf3c`](#insn-00aecf3c)
  - `FALL_THROUGH` [`00aecf18`](#insn-00aecf18) → [`00aecf1c`](#insn-00aecf1c)
- ブロック [`00aecf1c`](#insn-00aecf1c) 範囲 `[['00aecf1c', '00aecf3b']]`
  - `FALL_THROUGH` [`00aecf38`](#insn-00aecf38) → [`00aecf3c`](#insn-00aecf3c)
- ブロック [`00aecf3c`](#insn-00aecf3c) 範囲 `[['00aecf3c', '00aecf47']]`
  - `FALL_THROUGH` [`00aecf44`](#insn-00aecf44) → [`00aecf48`](#insn-00aecf48)
- ブロック [`00aecf48`](#insn-00aecf48) 範囲 `[['00aecf48', '00aecf57']]`

## 命令位置別の参照

- [`00aecebc`](#insn-00aecebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecec0`](#insn-00aecec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecec4`](#insn-00aecec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeced0`](#insn-00aeced0) → `010a09d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeced4`](#insn-00aeced4) → [`00aecee0`](#insn-00aecee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecedc`](#insn-00aecedc) → [`00aecf48`](#insn-00aecf48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecef0`](#insn-00aecef0) → `010a09c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecf18`](#insn-00aecf18) → [`00aecf3c`](#insn-00aecf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf44`](#insn-00aecf44) → `010a09d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecf48`](#insn-00aecf48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf4c`](#insn-00aecf4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecebc`](#insn-00aecebc)

~~~json
{
  "source": "00aecebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecec0`](#insn-00aecec0)

~~~json
{
  "source": "00aecec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecec4`](#insn-00aecec4)

~~~json
{
  "source": "00aecec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeced0`](#insn-00aeced0)

~~~json
{
  "source": "00aeced0",
  "target": "010a09d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeced4`](#insn-00aeced4)

~~~json
{
  "source": "00aeced4",
  "target": "00aecee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecedc`](#insn-00aecedc)

~~~json
{
  "source": "00aecedc",
  "target": "00aecf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecef0`](#insn-00aecef0)

~~~json
{
  "source": "00aecef0",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf18`](#insn-00aecf18)

~~~json
{
  "source": "00aecf18",
  "target": "00aecf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf44`](#insn-00aecf44)

~~~json
{
  "source": "00aecf44",
  "target": "010a09d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf48`](#insn-00aecf48)

~~~json
{
  "source": "00aecf48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf4c`](#insn-00aecf4c)

~~~json
{
  "source": "00aecf4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
