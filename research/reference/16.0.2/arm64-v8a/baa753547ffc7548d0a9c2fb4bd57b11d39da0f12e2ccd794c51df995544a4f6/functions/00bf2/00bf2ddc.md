# 00bf2ddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf2d40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-75e17246050cbef281a222ecca341f0f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf3dd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3dd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-b29dbbc3048d2eaf98169fc1179adb5e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf2ddc",
  "name": "_ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d",
  "source_text_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf2ddc",
        "00bf2e77"
      ]
    ],
    "bytes_sha256": "9e711d9d609bd937d503e66972c919ef2c44753879853541c35597575c785f91",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58520](../00c58/00c58520.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 848 bytes

~~~c

long _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm
               (byte *param_1,wchar_t *param_2,ulong param_3,size_t param_4)

{
  ulong uVar1;
  byte *pbVar2;
  wchar_t *pwVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  uVar1 = (ulong)(*param_1 >> 1);
  pbVar2 = param_1 + 4;
  if ((*param_1 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
    pbVar2 = *(byte **)(param_1 + 0x10);
  }
  if (param_3 < uVar1) {
    pwVar4 = (wchar_t *)(pbVar2 + param_3 * 4);
    if (param_4 == 0) {
LAB_00bf2e58:
      return (long)pwVar4 - (long)pbVar2 >> 2;
    }
    lVar5 = uVar1 * 4 + param_3 * -4;
    do {
      pwVar3 = wmemchr(param_2,*pwVar4,param_4);
      if (pwVar3 == (wchar_t *)0x0) goto LAB_00bf2e58;
      lVar5 = lVar5 + -4;
      pwVar4 = pwVar4 + 1;
    } while (lVar5 != 0);
  }
  return -1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf2ddc"></a> `00bf2ddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf2de0"></a> `00bf2de0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bf2de4"></a> `00bf2de4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2de8"></a> `00bf2de8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf2dec"></a> `00bf2dec` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf2df0"></a> `00bf2df0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf2df4"></a> `00bf2df4` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bf2df8"></a> `00bf2df8` | `09 ac 40 a9` | ldp x9,x11,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bf2dfc"></a> `00bf2dfc` | `0c 10 00 91` | add x12,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf2e00"></a> `00bf2e00` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e04"></a> `00bf2e04` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf2e08"></a> `00bf2e08` | `95 01 8b 9a` | csel x21,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00bf2e0c"></a> `00bf2e0c` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf2e10"></a> `00bf2e10` | `1f 01 02 eb` | cmp x8,x2 | `FALL_THROUGH`
<a id="insn-00bf2e14"></a> `00bf2e14` | `e9 01 00 54` | b.ls 0x00bf2e50 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e18"></a> `00bf2e18` | `b6 0a 02 8b` | add x22,x21,x2, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2e1c"></a> `00bf2e1c` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bf2e20"></a> `00bf2e20` | `c3 01 00 b4` | cbz x3,0x00bf2e58 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e24"></a> `00bf2e24` | `08 f5 7e d3` | lsl x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bf2e28"></a> `00bf2e28` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf2e2c"></a> `00bf2e2c` | `17 09 02 cb` | sub x23,x8,x2, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf2e30"></a> `00bf2e30` | `c1 02 40 b9` | ldr w1,[x22] | `FALL_THROUGH`
<a id="insn-00bf2e34"></a> `00bf2e34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf2e38"></a> `00bf2e38` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bf2e3c"></a> `00bf2e3c` | `b9 95 01 94` | bl 0x00c58520 | `UNCONDITIONAL_CALL`
<a id="insn-00bf2e40"></a> `00bf2e40` | `c0 00 00 b4` | cbz x0,0x00bf2e58 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e44"></a> `00bf2e44` | `f7 12 00 f1` | subs x23,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00bf2e48"></a> `00bf2e48` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bf2e4c"></a> `00bf2e4c` | `21 ff ff 54` | b.ne 0x00bf2e30 | `CONDITIONAL_JUMP`
<a id="insn-00bf2e50"></a> `00bf2e50` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00bf2e54"></a> `00bf2e54` | `03 00 00 14` | b 0x00bf2e60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf2e58"></a> `00bf2e58` | `c8 02 15 cb` | sub x8,x22,x21 | `FALL_THROUGH`
<a id="insn-00bf2e5c"></a> `00bf2e5c` | `00 fd 42 93` | asr x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bf2e60"></a> `00bf2e60` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf2e64"></a> `00bf2e64` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf2e68"></a> `00bf2e68` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf2e6c"></a> `00bf2e6c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bf2e70"></a> `00bf2e70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf2e74"></a> `00bf2e74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf2ddc`](#insn-00bf2ddc) 範囲 `[['00bf2ddc', '00bf2e17']]`
  - `CONDITIONAL_JUMP` [`00bf2e14`](#insn-00bf2e14) → [`00bf2e50`](#insn-00bf2e50)
  - `FALL_THROUGH` [`00bf2e14`](#insn-00bf2e14) → [`00bf2e18`](#insn-00bf2e18)
- ブロック [`00bf2e18`](#insn-00bf2e18) 範囲 `[['00bf2e18', '00bf2e23']]`
  - `CONDITIONAL_JUMP` [`00bf2e20`](#insn-00bf2e20) → [`00bf2e58`](#insn-00bf2e58)
  - `FALL_THROUGH` [`00bf2e20`](#insn-00bf2e20) → [`00bf2e24`](#insn-00bf2e24)
- ブロック [`00bf2e24`](#insn-00bf2e24) 範囲 `[['00bf2e24', '00bf2e2f']]`
  - `FALL_THROUGH` [`00bf2e2c`](#insn-00bf2e2c) → [`00bf2e30`](#insn-00bf2e30)
- ブロック [`00bf2e30`](#insn-00bf2e30) 範囲 `[['00bf2e30', '00bf2e43']]`
  - `CONDITIONAL_JUMP` [`00bf2e40`](#insn-00bf2e40) → [`00bf2e58`](#insn-00bf2e58)
  - `FALL_THROUGH` [`00bf2e40`](#insn-00bf2e40) → [`00bf2e44`](#insn-00bf2e44)
- ブロック [`00bf2e44`](#insn-00bf2e44) 範囲 `[['00bf2e44', '00bf2e4f']]`
  - `CONDITIONAL_JUMP` [`00bf2e4c`](#insn-00bf2e4c) → [`00bf2e30`](#insn-00bf2e30)
  - `FALL_THROUGH` [`00bf2e4c`](#insn-00bf2e4c) → [`00bf2e50`](#insn-00bf2e50)
- ブロック [`00bf2e50`](#insn-00bf2e50) 範囲 `[['00bf2e50', '00bf2e57']]`
  - `UNCONDITIONAL_JUMP` [`00bf2e54`](#insn-00bf2e54) → [`00bf2e60`](#insn-00bf2e60)
- ブロック [`00bf2e58`](#insn-00bf2e58) 範囲 `[['00bf2e58', '00bf2e5f']]`
  - `FALL_THROUGH` [`00bf2e5c`](#insn-00bf2e5c) → [`00bf2e60`](#insn-00bf2e60)
- ブロック [`00bf2e60`](#insn-00bf2e60) 範囲 `[['00bf2e60', '00bf2e77']]`

## 命令位置別の参照

- [`00bf2de0`](#insn-00bf2de0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2de4`](#insn-00bf2de4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2de8`](#insn-00bf2de8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2dec`](#insn-00bf2dec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e14`](#insn-00bf2e14) → [`00bf2e50`](#insn-00bf2e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e20`](#insn-00bf2e20) → [`00bf2e58`](#insn-00bf2e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e3c`](#insn-00bf2e3c) → [`00c58520`](../00c58/00c58520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58520` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e40`](#insn-00bf2e40) → [`00bf2e58`](#insn-00bf2e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e4c`](#insn-00bf2e4c) → [`00bf2e30`](#insn-00bf2e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e54`](#insn-00bf2e54) → [`00bf2e60`](#insn-00bf2e60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e60`](#insn-00bf2e60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e64`](#insn-00bf2e64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e68`](#insn-00bf2e68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf2e6c`](#insn-00bf2e6c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf2de0`](#insn-00bf2de0)

~~~json
{
  "source": "00bf2de0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2de4`](#insn-00bf2de4)

~~~json
{
  "source": "00bf2de4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2de8`](#insn-00bf2de8)

~~~json
{
  "source": "00bf2de8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2dec`](#insn-00bf2dec)

~~~json
{
  "source": "00bf2dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e14`](#insn-00bf2e14)

~~~json
{
  "source": "00bf2e14",
  "target": "00bf2e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e20`](#insn-00bf2e20)

~~~json
{
  "source": "00bf2e20",
  "target": "00bf2e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e3c`](#insn-00bf2e3c)

~~~json
{
  "source": "00bf2e3c",
  "target": "00c58520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf2e40`](#insn-00bf2e40)

~~~json
{
  "source": "00bf2e40",
  "target": "00bf2e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e4c`](#insn-00bf2e4c)

~~~json
{
  "source": "00bf2e4c",
  "target": "00bf2e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e54`](#insn-00bf2e54)

~~~json
{
  "source": "00bf2e54",
  "target": "00bf2e60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e60`](#insn-00bf2e60)

~~~json
{
  "source": "00bf2e60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e64`](#insn-00bf2e64)

~~~json
{
  "source": "00bf2e64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e68`](#insn-00bf2e68)

~~~json
{
  "source": "00bf2e68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf2e6c`](#insn-00bf2e6c)

~~~json
{
  "source": "00bf2e6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
