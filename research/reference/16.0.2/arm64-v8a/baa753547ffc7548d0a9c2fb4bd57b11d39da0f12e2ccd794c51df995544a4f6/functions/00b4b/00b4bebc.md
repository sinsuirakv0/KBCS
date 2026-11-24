# 00b4bebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4be20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-52cec2e9fdb0944ebfc31e7983cfd759)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4ceb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ceb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-eabf524fe2e1fb001a4ac0420c9579ca)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4bebc",
  "name": "_ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2cecbbeea3e2deca563f63473e337d99f6807104733aaa1a75eb2d487f00556",
  "source_text_sha256": "b2cecbbeea3e2deca563f63473e337d99f6807104733aaa1a75eb2d487f00556",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4bebc",
        "00b4bf57"
      ]
    ],
    "bytes_sha256": "2ebaa7930b0e26f8c75608f6a9a14b5ce5e181ba1350c833a29c5fffdacf7f0d",
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

## 疑似コード / UTF-8 606 bytes

~~~c

bool _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_01125cc0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01125cb8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_01125cc0 = iVar3 == 0;
    bVar2 = (bool)DAT_01125cc0;
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
<a id="insn-00b4bebc"></a> `00b4bebc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4bec0"></a> `00b4bec0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bec4"></a> `00b4bec4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4bec8"></a> `00b4bec8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4becc"></a> `00b4becc` | `d5 2e 00 d0` | adrp x21,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bed0"></a> `00b4bed0` | `a8 02 73 39` | ldrb w8,[x21, #0xcc0] | `FALL_THROUGH`
<a id="insn-00b4bed4"></a> `00b4bed4` | `68 00 00 34` | cbz w8,0x00b4bee0 | `CONDITIONAL_JUMP`
<a id="insn-00b4bed8"></a> `00b4bed8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b4bedc"></a> `00b4bedc` | `1b 00 00 14` | b 0x00b4bf48 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4bee0"></a> `00b4bee0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b4bee4"></a> `00b4bee4` | `c9 2e 00 d0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bee8"></a> `00b4bee8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00b4beec"></a> `00b4beec` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00b4bef0"></a> `00b4bef0` | `21 5d 46 f9` | ldr x1,[x9, #0xcb8] | `FALL_THROUGH`
<a id="insn-00b4bef4"></a> `00b4bef4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00b4bef8"></a> `00b4bef8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4befc"></a> `00b4befc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf00"></a> `00b4bf00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf04"></a> `00b4bf04` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b4bf08"></a> `00b4bf08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf0c"></a> `00b4bf0c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4bf10"></a> `00b4bf10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf14"></a> `00b4bf14` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4bf18"></a> `00b4bf18` | `20 01 00 54` | b.eq 0x00b4bf3c | `CONDITIONAL_JUMP`
<a id="insn-00b4bf1c"></a> `00b4bf1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf20"></a> `00b4bf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf24"></a> `00b4bf24` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4bf28"></a> `00b4bf28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf2c"></a> `00b4bf2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf30"></a> `00b4bf30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf34"></a> `00b4bf34` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4bf38"></a> `00b4bf38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf3c"></a> `00b4bf3c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00b4bf40"></a> `00b4bf40` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00b4bf44"></a> `00b4bf44` | `a0 02 33 39` | strb w0,[x21, #0xcc0] | `FALL_THROUGH`
<a id="insn-00b4bf48"></a> `00b4bf48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4bf4c"></a> `00b4bf4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bf50"></a> `00b4bf50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4bf54"></a> `00b4bf54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4bebc`](#insn-00b4bebc) 範囲 `[['00b4bebc', '00b4bed7']]`
  - `CONDITIONAL_JUMP` [`00b4bed4`](#insn-00b4bed4) → [`00b4bee0`](#insn-00b4bee0)
  - `FALL_THROUGH` [`00b4bed4`](#insn-00b4bed4) → [`00b4bed8`](#insn-00b4bed8)
- ブロック [`00b4bed8`](#insn-00b4bed8) 範囲 `[['00b4bed8', '00b4bedf']]`
  - `UNCONDITIONAL_JUMP` [`00b4bedc`](#insn-00b4bedc) → [`00b4bf48`](#insn-00b4bf48)
- ブロック [`00b4bee0`](#insn-00b4bee0) 範囲 `[['00b4bee0', '00b4bf1b']]`
  - `CONDITIONAL_JUMP` [`00b4bf18`](#insn-00b4bf18) → [`00b4bf3c`](#insn-00b4bf3c)
  - `FALL_THROUGH` [`00b4bf18`](#insn-00b4bf18) → [`00b4bf1c`](#insn-00b4bf1c)
- ブロック [`00b4bf1c`](#insn-00b4bf1c) 範囲 `[['00b4bf1c', '00b4bf3b']]`
  - `FALL_THROUGH` [`00b4bf38`](#insn-00b4bf38) → [`00b4bf3c`](#insn-00b4bf3c)
- ブロック [`00b4bf3c`](#insn-00b4bf3c) 範囲 `[['00b4bf3c', '00b4bf47']]`
  - `FALL_THROUGH` [`00b4bf44`](#insn-00b4bf44) → [`00b4bf48`](#insn-00b4bf48)
- ブロック [`00b4bf48`](#insn-00b4bf48) 範囲 `[['00b4bf48', '00b4bf57']]`

## 命令位置別の参照

- [`00b4bebc`](#insn-00b4bebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bec0`](#insn-00b4bec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bec4`](#insn-00b4bec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bed0`](#insn-00b4bed0) → `01125cc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4bed4`](#insn-00b4bed4) → [`00b4bee0`](#insn-00b4bee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bedc`](#insn-00b4bedc) → [`00b4bf48`](#insn-00b4bf48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bef0`](#insn-00b4bef0) → `01125cb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bf18`](#insn-00b4bf18) → [`00b4bf3c`](#insn-00b4bf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bf44`](#insn-00b4bf44) → `01125cc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4bf48`](#insn-00b4bf48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bf4c`](#insn-00b4bf4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4bebc`](#insn-00b4bebc)

~~~json
{
  "source": "00b4bebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bec0`](#insn-00b4bec0)

~~~json
{
  "source": "00b4bec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bec4`](#insn-00b4bec4)

~~~json
{
  "source": "00b4bec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bed0`](#insn-00b4bed0)

~~~json
{
  "source": "00b4bed0",
  "target": "01125cc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125cc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bed4`](#insn-00b4bed4)

~~~json
{
  "source": "00b4bed4",
  "target": "00b4bee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bedc`](#insn-00b4bedc)

~~~json
{
  "source": "00b4bedc",
  "target": "00b4bf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bef0`](#insn-00b4bef0)

~~~json
{
  "source": "00b4bef0",
  "target": "01125cb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125cb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bf18`](#insn-00b4bf18)

~~~json
{
  "source": "00b4bf18",
  "target": "00b4bf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bf44`](#insn-00b4bf44)

~~~json
{
  "source": "00b4bf44",
  "target": "01125cc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125cc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bf48`](#insn-00b4bf48)

~~~json
{
  "source": "00b4bf48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bf4c`](#insn-00b4bf4c)

~~~json
{
  "source": "00b4bf4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
