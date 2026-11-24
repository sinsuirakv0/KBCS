# 00adaafc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adaab8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaab8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0007.md#compare-8301ce487f39de0af5b159b3343c9c9c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a4d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a4d4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0003.md#compare-b29ca04217424dd2b67bf4d0004637dd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adaafc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edbe38aa15474fa56acc4f265088daf9a4580a132c62cbc60847b690940ba761",
  "source_text_sha256": "edbe38aa15474fa56acc4f265088daf9a4580a132c62cbc60847b690940ba761",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adaafc",
        "00adab63"
      ]
    ],
    "bytes_sha256": "45e77755ce2b5fa561b972b00d7b6004cf070cc06e4048a267c9215ce162c223",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 550 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect
               (undefined8 param_1,undefined8 param_2,char param_3)

{
  long lVar1;
  undefined1 local_2c [4];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_0109ff90 != (long *)0x0) {
    local_2c[0] = param_3 != '\0';
    (**(code **)(*DAT_0109ff90 + 0x30))(DAT_0109ff90,local_2c);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adaafc"></a> `00adaafc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adab00"></a> `00adab00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adab04"></a> `00adab04` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adab08"></a> `00adab08` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00adab0c"></a> `00adab0c` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adab10"></a> `00adab10` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00adab14"></a> `00adab14` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adab18"></a> `00adab18` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adab1c"></a> `00adab1c` | `00 c9 47 f9` | ldr x0,[x8, #0xf90] | `FALL_THROUGH`
<a id="insn-00adab20"></a> `00adab20` | `00 01 00 b4` | cbz x0,0x00adab40 | `CONDITIONAL_JUMP`
<a id="insn-00adab24"></a> `00adab24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adab28"></a> `00adab28` | `5f 1c 00 72` | tst w2,#0xff | `FALL_THROUGH`
<a id="insn-00adab2c"></a> `00adab2c` | `e1 13 00 91` | add x1,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00adab30"></a> `00adab30` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00adab34"></a> `00adab34` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adab38"></a> `00adab38` | `e9 13 00 39` | strb w9,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00adab3c"></a> `00adab3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adab40"></a> `00adab40` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00adab44"></a> `00adab44` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adab48"></a> `00adab48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adab4c"></a> `00adab4c` | `a1 00 00 54` | b.ne 0x00adab60 | `CONDITIONAL_JUMP`
<a id="insn-00adab50"></a> `00adab50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adab54"></a> `00adab54` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adab58"></a> `00adab58` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adab5c"></a> `00adab5c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adab60"></a> `00adab60` | `4c 01 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adaafc`](#insn-00adaafc) 範囲 `[['00adaafc', '00adab23']]`
  - `CONDITIONAL_JUMP` [`00adab20`](#insn-00adab20) → [`00adab40`](#insn-00adab40)
  - `FALL_THROUGH` [`00adab20`](#insn-00adab20) → [`00adab24`](#insn-00adab24)
- ブロック [`00adab24`](#insn-00adab24) 範囲 `[['00adab24', '00adab3f']]`
  - `FALL_THROUGH` [`00adab3c`](#insn-00adab3c) → [`00adab40`](#insn-00adab40)
- ブロック [`00adab40`](#insn-00adab40) 範囲 `[['00adab40', '00adab4f']]`
  - `CONDITIONAL_JUMP` [`00adab4c`](#insn-00adab4c) → [`00adab60`](#insn-00adab60)
  - `FALL_THROUGH` [`00adab4c`](#insn-00adab4c) → [`00adab50`](#insn-00adab50)
- ブロック [`00adab50`](#insn-00adab50) 範囲 `[['00adab50', '00adab5f']]`
- ブロック [`00adab60`](#insn-00adab60) 範囲 `[['00adab60', '00adab63']]`

## 命令位置別の参照

- [`00adab00`](#insn-00adab00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab04`](#insn-00adab04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab14`](#insn-00adab14) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab1c`](#insn-00adab1c) → `0109ff90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adab20`](#insn-00adab20) → [`00adab40`](#insn-00adab40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab38`](#insn-00adab38) → `Stack[-0x2c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab44`](#insn-00adab44) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab4c`](#insn-00adab4c) → [`00adab60`](#insn-00adab60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab50`](#insn-00adab50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab54`](#insn-00adab54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab60`](#insn-00adab60) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adab00`](#insn-00adab00)

~~~json
{
  "source": "00adab00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab04`](#insn-00adab04)

~~~json
{
  "source": "00adab04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab14`](#insn-00adab14)

~~~json
{
  "source": "00adab14",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab1c`](#insn-00adab1c)

~~~json
{
  "source": "00adab1c",
  "target": "0109ff90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adab20`](#insn-00adab20)

~~~json
{
  "source": "00adab20",
  "target": "00adab40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab38`](#insn-00adab38)

~~~json
{
  "source": "00adab38",
  "target": "Stack[-0x2c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab44`](#insn-00adab44)

~~~json
{
  "source": "00adab44",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab4c`](#insn-00adab4c)

~~~json
{
  "source": "00adab4c",
  "target": "00adab60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab50`](#insn-00adab50)

~~~json
{
  "source": "00adab50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab54`](#insn-00adab54)

~~~json
{
  "source": "00adab54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab60`](#insn-00adab60)

~~~json
{
  "source": "00adab60",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
