# 00aeaac8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeaa84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-431845c8432e70b62db6d4ea3d8d1f3e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4a84c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-f932becfd2c2fac084861805b1ea4e44)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaac8",
  "name": "_ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1f36e689659c81a222175c1834bf9a35fdbd7d79717816b328225282938d0a6",
  "source_text_sha256": "d1f36e689659c81a222175c1834bf9a35fdbd7d79717816b328225282938d0a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaac8",
        "00aeab67"
      ]
    ],
    "bytes_sha256": "fed5b52d9cd21ded1551d6a22804036da1b72089936fd3775dec22201b917fe6",
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

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0828 != 0) {
    if (DAT_010a0830 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0830 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0828);
    DAT_010a0828 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaac8"></a> `00aeaac8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeaacc"></a> `00aeaacc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaad0"></a> `00aeaad0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaad4"></a> `00aeaad4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeaad8"></a> `00aeaad8` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaadc"></a> `00aeaadc` | `81 16 44 f9` | ldr x1,[x20, #0x828] | `FALL_THROUGH`
<a id="insn-00aeaae0"></a> `00aeaae0` | `c1 03 00 b4` | cbz x1,0x00aeab58 | `CONDITIONAL_JUMP`
<a id="insn-00aeaae4"></a> `00aeaae4` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaae8"></a> `00aeaae8` | `a8 c2 60 39` | ldrb w8,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00aeaaec"></a> `00aeaaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeaaf0"></a> `00aeaaf0` | `c8 00 00 34` | cbz w8,0x00aeab08 | `CONDITIONAL_JUMP`
<a id="insn-00aeaaf4"></a> `00aeaaf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaaf8"></a> `00aeaaf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaafc"></a> `00aeaafc` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aeab00"></a> `00aeab00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeab04"></a> `00aeab04` | `bf c2 20 39` | strb wzr,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00aeab08"></a> `00aeab08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeab0c"></a> `00aeab0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeab10"></a> `00aeab10` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeab14"></a> `00aeab14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeab18"></a> `00aeab18` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeab1c"></a> `00aeab1c` | `20 01 00 54` | b.eq 0x00aeab40 | `CONDITIONAL_JUMP`
<a id="insn-00aeab20"></a> `00aeab20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeab24"></a> `00aeab24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeab28"></a> `00aeab28` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeab2c"></a> `00aeab2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeab30"></a> `00aeab30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeab34"></a> `00aeab34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeab38"></a> `00aeab38` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeab3c"></a> `00aeab3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeab40"></a> `00aeab40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeab44"></a> `00aeab44` | `81 16 44 f9` | ldr x1,[x20, #0x828] | `FALL_THROUGH`
<a id="insn-00aeab48"></a> `00aeab48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeab4c"></a> `00aeab4c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeab50"></a> `00aeab50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeab54"></a> `00aeab54` | `9f 16 04 f9` | str xzr,[x20, #0x828] | `FALL_THROUGH`
<a id="insn-00aeab58"></a> `00aeab58` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeab5c"></a> `00aeab5c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeab60"></a> `00aeab60` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeab64"></a> `00aeab64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaac8`](#insn-00aeaac8) 範囲 `[['00aeaac8', '00aeaae3']]`
  - `CONDITIONAL_JUMP` [`00aeaae0`](#insn-00aeaae0) → [`00aeab58`](#insn-00aeab58)
  - `FALL_THROUGH` [`00aeaae0`](#insn-00aeaae0) → [`00aeaae4`](#insn-00aeaae4)
- ブロック [`00aeaae4`](#insn-00aeaae4) 範囲 `[['00aeaae4', '00aeaaf3']]`
  - `CONDITIONAL_JUMP` [`00aeaaf0`](#insn-00aeaaf0) → [`00aeab08`](#insn-00aeab08)
  - `FALL_THROUGH` [`00aeaaf0`](#insn-00aeaaf0) → [`00aeaaf4`](#insn-00aeaaf4)
- ブロック [`00aeaaf4`](#insn-00aeaaf4) 範囲 `[['00aeaaf4', '00aeab07']]`
  - `FALL_THROUGH` [`00aeab04`](#insn-00aeab04) → [`00aeab08`](#insn-00aeab08)
- ブロック [`00aeab08`](#insn-00aeab08) 範囲 `[['00aeab08', '00aeab1f']]`
  - `CONDITIONAL_JUMP` [`00aeab1c`](#insn-00aeab1c) → [`00aeab40`](#insn-00aeab40)
  - `FALL_THROUGH` [`00aeab1c`](#insn-00aeab1c) → [`00aeab20`](#insn-00aeab20)
- ブロック [`00aeab20`](#insn-00aeab20) 範囲 `[['00aeab20', '00aeab3f']]`
  - `FALL_THROUGH` [`00aeab3c`](#insn-00aeab3c) → [`00aeab40`](#insn-00aeab40)
- ブロック [`00aeab40`](#insn-00aeab40) 範囲 `[['00aeab40', '00aeab57']]`
  - `FALL_THROUGH` [`00aeab54`](#insn-00aeab54) → [`00aeab58`](#insn-00aeab58)
- ブロック [`00aeab58`](#insn-00aeab58) 範囲 `[['00aeab58', '00aeab67']]`

## 命令位置別の参照

- [`00aeaac8`](#insn-00aeaac8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaacc`](#insn-00aeaacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaad0`](#insn-00aeaad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaadc`](#insn-00aeaadc) → `010a0828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaae0`](#insn-00aeaae0) → [`00aeab58`](#insn-00aeab58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaae8`](#insn-00aeaae8) → `010a0830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeaaf0`](#insn-00aeaaf0) → [`00aeab08`](#insn-00aeab08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeab04`](#insn-00aeab04) → `010a0830`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeab1c`](#insn-00aeab1c) → [`00aeab40`](#insn-00aeab40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeab44`](#insn-00aeab44) → `010a0828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeab54`](#insn-00aeab54) → `010a0828`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeab58`](#insn-00aeab58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeab5c`](#insn-00aeab5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaac8`](#insn-00aeaac8)

~~~json
{
  "source": "00aeaac8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaacc`](#insn-00aeaacc)

~~~json
{
  "source": "00aeaacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaad0`](#insn-00aeaad0)

~~~json
{
  "source": "00aeaad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaadc`](#insn-00aeaadc)

~~~json
{
  "source": "00aeaadc",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaae0`](#insn-00aeaae0)

~~~json
{
  "source": "00aeaae0",
  "target": "00aeab58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaae8`](#insn-00aeaae8)

~~~json
{
  "source": "00aeaae8",
  "target": "010a0830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaaf0`](#insn-00aeaaf0)

~~~json
{
  "source": "00aeaaf0",
  "target": "00aeab08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeab04`](#insn-00aeab04)

~~~json
{
  "source": "00aeab04",
  "target": "010a0830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeab1c`](#insn-00aeab1c)

~~~json
{
  "source": "00aeab1c",
  "target": "00aeab40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeab44`](#insn-00aeab44)

~~~json
{
  "source": "00aeab44",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeab54`](#insn-00aeab54)

~~~json
{
  "source": "00aeab54",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeab58`](#insn-00aeab58)

~~~json
{
  "source": "00aeab58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeab5c`](#insn-00aeab5c)

~~~json
{
  "source": "00aeab5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
