# 00aecbb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecb6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-39153b1612947b4d10444c2287c1458c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4c934`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-3b3de6611464f07478e9882884bb6a5b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecbb0",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6015ebc3d0f590f5ba960a70ad89f920522a56f7176b725409a6622649a81f4b",
  "source_text_sha256": "6015ebc3d0f590f5ba960a70ad89f920522a56f7176b725409a6622649a81f4b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecbb0",
        "00aecc4f"
      ]
    ],
    "bytes_sha256": "e346c21d11f0e38aff28b1bba0a9c4cbe5e34ffa089fa162b023644b16aa4177",
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
  
                    /* try { // try from 00aecbb4 to 00becbc3 has its CatchHandler @ 00af1a84 */
  if (DAT_010a09a8 != 0) {
    if (DAT_010a09b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a09b0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a09a8);
    DAT_010a09a8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecbb0"></a> `00aecbb0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecbb4"></a> `00aecbb4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecbb8"></a> `00aecbb8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecbbc"></a> `00aecbbc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecbc0"></a> `00aecbc0` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecbc4"></a> `00aecbc4` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecbc8"></a> `00aecbc8` | `c1 03 00 b4` | cbz x1,0x00aecc40 | `CONDITIONAL_JUMP`
<a id="insn-00aecbcc"></a> `00aecbcc` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecbd0"></a> `00aecbd0` | `a8 c2 66 39` | ldrb w8,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aecbd4"></a> `00aecbd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecbd8"></a> `00aecbd8` | `c8 00 00 34` | cbz w8,0x00aecbf0 | `CONDITIONAL_JUMP`
<a id="insn-00aecbdc"></a> `00aecbdc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbe0"></a> `00aecbe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbe4"></a> `00aecbe4` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aecbe8"></a> `00aecbe8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecbec"></a> `00aecbec` | `bf c2 26 39` | strb wzr,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aecbf0"></a> `00aecbf0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecbf4"></a> `00aecbf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecbf8"></a> `00aecbf8` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aecbfc"></a> `00aecbfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecc00"></a> `00aecc00` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecc04"></a> `00aecc04` | `20 01 00 54` | b.eq 0x00aecc28 | `CONDITIONAL_JUMP`
<a id="insn-00aecc08"></a> `00aecc08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecc0c"></a> `00aecc0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc10"></a> `00aecc10` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aecc14"></a> `00aecc14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecc18"></a> `00aecc18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecc1c"></a> `00aecc1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc20"></a> `00aecc20` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecc24"></a> `00aecc24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecc28"></a> `00aecc28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecc2c"></a> `00aecc2c` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecc30"></a> `00aecc30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecc34"></a> `00aecc34` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aecc38"></a> `00aecc38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecc3c"></a> `00aecc3c` | `9f d6 04 f9` | str xzr,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecc40"></a> `00aecc40` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecc44"></a> `00aecc44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecc48"></a> `00aecc48` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecc4c"></a> `00aecc4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecbb0`](#insn-00aecbb0) 範囲 `[['00aecbb0', '00aecbb3']]`
  - `FALL_THROUGH` [`00aecbb0`](#insn-00aecbb0) → [`00aecbb4`](#insn-00aecbb4)
- ブロック [`00aecbb4`](#insn-00aecbb4) 範囲 `[['00aecbb4', '00aecbcb']]`
  - `CONDITIONAL_JUMP` [`00aecbc8`](#insn-00aecbc8) → [`00aecc40`](#insn-00aecc40)
  - `FALL_THROUGH` [`00aecbc8`](#insn-00aecbc8) → [`00aecbcc`](#insn-00aecbcc)
- ブロック [`00aecbcc`](#insn-00aecbcc) 範囲 `[['00aecbcc', '00aecbdb']]`
  - `CONDITIONAL_JUMP` [`00aecbd8`](#insn-00aecbd8) → [`00aecbf0`](#insn-00aecbf0)
  - `FALL_THROUGH` [`00aecbd8`](#insn-00aecbd8) → [`00aecbdc`](#insn-00aecbdc)
- ブロック [`00aecbdc`](#insn-00aecbdc) 範囲 `[['00aecbdc', '00aecbef']]`
  - `FALL_THROUGH` [`00aecbec`](#insn-00aecbec) → [`00aecbf0`](#insn-00aecbf0)
- ブロック [`00aecbf0`](#insn-00aecbf0) 範囲 `[['00aecbf0', '00aecc07']]`
  - `CONDITIONAL_JUMP` [`00aecc04`](#insn-00aecc04) → [`00aecc28`](#insn-00aecc28)
  - `FALL_THROUGH` [`00aecc04`](#insn-00aecc04) → [`00aecc08`](#insn-00aecc08)
- ブロック [`00aecc08`](#insn-00aecc08) 範囲 `[['00aecc08', '00aecc27']]`
  - `FALL_THROUGH` [`00aecc24`](#insn-00aecc24) → [`00aecc28`](#insn-00aecc28)
- ブロック [`00aecc28`](#insn-00aecc28) 範囲 `[['00aecc28', '00aecc3f']]`
  - `FALL_THROUGH` [`00aecc3c`](#insn-00aecc3c) → [`00aecc40`](#insn-00aecc40)
- ブロック [`00aecc40`](#insn-00aecc40) 範囲 `[['00aecc40', '00aecc4f']]`

## 命令位置別の参照

- [`00aecbb0`](#insn-00aecbb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbb4`](#insn-00aecbb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbb8`](#insn-00aecbb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbc4`](#insn-00aecbc4) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecbc8`](#insn-00aecbc8) → [`00aecc40`](#insn-00aecc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbd0`](#insn-00aecbd0) → `010a09b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecbd8`](#insn-00aecbd8) → [`00aecbf0`](#insn-00aecbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbec`](#insn-00aecbec) → `010a09b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecc04`](#insn-00aecc04) → [`00aecc28`](#insn-00aecc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc2c`](#insn-00aecc2c) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc3c`](#insn-00aecc3c) → `010a09a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecc40`](#insn-00aecc40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc44`](#insn-00aecc44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecbb0`](#insn-00aecbb0)

~~~json
{
  "source": "00aecbb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbb4`](#insn-00aecbb4)

~~~json
{
  "source": "00aecbb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbb8`](#insn-00aecbb8)

~~~json
{
  "source": "00aecbb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbc4`](#insn-00aecbc4)

~~~json
{
  "source": "00aecbc4",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecbc8`](#insn-00aecbc8)

~~~json
{
  "source": "00aecbc8",
  "target": "00aecc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbd0`](#insn-00aecbd0)

~~~json
{
  "source": "00aecbd0",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecbd8`](#insn-00aecbd8)

~~~json
{
  "source": "00aecbd8",
  "target": "00aecbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbec`](#insn-00aecbec)

~~~json
{
  "source": "00aecbec",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc04`](#insn-00aecc04)

~~~json
{
  "source": "00aecc04",
  "target": "00aecc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc2c`](#insn-00aecc2c)

~~~json
{
  "source": "00aecc2c",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc3c`](#insn-00aecc3c)

~~~json
{
  "source": "00aecc3c",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecc40`](#insn-00aecc40)

~~~json
{
  "source": "00aecc40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc44`](#insn-00aecc44)

~~~json
{
  "source": "00aecc44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
