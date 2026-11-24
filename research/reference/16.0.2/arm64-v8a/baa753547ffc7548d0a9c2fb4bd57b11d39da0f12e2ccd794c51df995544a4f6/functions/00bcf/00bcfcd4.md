# 00bcfcd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfc38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfc38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-f0f96190a80622e1bef80bc1597d4fb8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0cc8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0cc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-f080c3907088fa470acd3697bd33a123)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfcd4",
  "name": "_ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85482b0b1c773adf6c6a6f341e9d2aef955fa3b1ab594b0b984525cb1477f947",
  "source_text_sha256": "85482b0b1c773adf6c6a6f341e9d2aef955fa3b1ab594b0b984525cb1477f947",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfcd4",
        "00bcfd4f"
      ]
    ],
    "bytes_sha256": "64be233382b3fe4edf146a293f1ba8742c3c9267312e85d109eb39f0c3b1c957",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5de10](../00c5d/00c5de10.md)

## 呼び出し先

- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aec0](../00c5a/00c5aec0.md)
- [00c5aed0](../00c5a/00c5aed0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1349 bytes

~~~c

void _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
                    /* try { // try from 00bcfd30 to 00ccff0f has its CatchHandler @ 00bcfd30
                       catch() { ... } // from try @ 00bcfd30 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcff1c with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcff98 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcfff8 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd01d8 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd0234 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd02f8 with catch @ 00bcfd30 */
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfcd4"></a> `00bcfcd4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcfcd8"></a> `00bcfcd8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfcdc"></a> `00bcfcdc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfce0"></a> `00bcfce0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfce4"></a> `00bcfce4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcfce8"></a> `00bcfce8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcfcec"></a> `00bcfcec` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcfcf0"></a> `00bcfcf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfcf4"></a> `00bcfcf4` | `13 2c 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfcf8"></a> `00bcfcf8` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfcfc"></a> `00bcfcfc` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcfd00"></a> `00bcfd00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfd04"></a> `00bcfd04` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcfd08"></a> `00bcfd08` | `72 2c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd0c"></a> `00bcfd0c` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd10"></a> `00bcfd10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfd14"></a> `00bcfd14` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd18"></a> `00bcfd18` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfd1c"></a> `00bcfd1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfd20"></a> `00bcfd20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcfd24"></a> `00bcfd24` | `67 2c 02 94` | bl 0x00c5aec0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd28"></a> `00bcfd28` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd2c"></a> `00bcfd2c` | `a0 00 00 b4` | cbz x0,0x00bcfd40 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd30"></a> `00bcfd30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfd34"></a> `00bcfd34` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bcfd38"></a> `00bcfd38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfd3c"></a> `00bcfd3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfd40"></a> `00bcfd40` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfd44"></a> `00bcfd44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd48"></a> `00bcfd48` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcfd4c"></a> `00bcfd4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfcd4`](#insn-00bcfcd4) 範囲 `[['00bcfcd4', '00bcfd2f']]`
  - `CONDITIONAL_JUMP` [`00bcfd2c`](#insn-00bcfd2c) → [`00bcfd40`](#insn-00bcfd40)
  - `FALL_THROUGH` [`00bcfd2c`](#insn-00bcfd2c) → [`00bcfd30`](#insn-00bcfd30)
- ブロック [`00bcfd30`](#insn-00bcfd30) 範囲 `[['00bcfd30', '00bcfd3f']]`
  - `FALL_THROUGH` [`00bcfd3c`](#insn-00bcfd3c) → [`00bcfd40`](#insn-00bcfd40)
- ブロック [`00bcfd40`](#insn-00bcfd40) 範囲 `[['00bcfd40', '00bcfd4f']]`

## 命令位置別の参照

- [`00bcfcd4`](#insn-00bcfcd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcd8`](#insn-00bcfcd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcdc`](#insn-00bcfcdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcf4`](#insn-00bcfcf4) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd08`](#insn-00bcfd08) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd24`](#insn-00bcfd24) → [`00c5aec0`](../00c5a/00c5aec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aec0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd2c`](#insn-00bcfd2c) → [`00bcfd40`](#insn-00bcfd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd40`](#insn-00bcfd40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd44`](#insn-00bcfd44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfcd4`](#insn-00bcfcd4)

~~~json
{
  "source": "00bcfcd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcd8`](#insn-00bcfcd8)

~~~json
{
  "source": "00bcfcd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcdc`](#insn-00bcfcdc)

~~~json
{
  "source": "00bcfcdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcf4`](#insn-00bcfcf4)

~~~json
{
  "source": "00bcfcf4",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd08`](#insn-00bcfd08)

~~~json
{
  "source": "00bcfd08",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd24`](#insn-00bcfd24)

~~~json
{
  "source": "00bcfd24",
  "target": "00c5aec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd2c`](#insn-00bcfd2c)

~~~json
{
  "source": "00bcfd2c",
  "target": "00bcfd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd40`](#insn-00bcfd40)

~~~json
{
  "source": "00bcfd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd44`](#insn-00bcfd44)

~~~json
{
  "source": "00bcfd44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
