# 00bdd5ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdc5f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc5f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-a338835bb59fc56916da40a1a2d8f167)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd5ec",
  "name": "_ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77a9dc3a2012e022ef9a8542c58646a7296bd77107822d146ae63ef9839fc9c0",
  "source_text_sha256": "77a9dc3a2012e022ef9a8542c58646a7296bd77107822d146ae63ef9839fc9c0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd5ec",
        "00bdd667"
      ]
    ],
    "bytes_sha256": "4b169fdb89d5f89b6ed65862122fc8aaa5e08ca48aa9fb60c7cc16b3a3cdd73c",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5eef0](../00c5e/00c5eef0.md)

## 呼び出し先

- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5be90](../00c5b/00c5be90.md)
- [00c5bea0](../00c5b/00c5bea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 649 bytes

~~~c

void _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
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
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd5ec"></a> `00bdd5ec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdd5f0"></a> `00bdd5f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd5f4"></a> `00bdd5f4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd5f8"></a> `00bdd5f8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdd5fc"></a> `00bdd5fc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bdd600"></a> `00bdd600` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bdd604"></a> `00bdd604` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bdd608"></a> `00bdd608` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd60c"></a> `00bdd60c` | `c1 f9 01 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd610"></a> `00bdd610` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdd614"></a> `00bdd614` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bdd618"></a> `00bdd618` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdd61c"></a> `00bdd61c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdd620"></a> `00bdd620` | `20 fa 01 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd624"></a> `00bdd624` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdd628"></a> `00bdd628` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdd62c"></a> `00bdd62c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd630"></a> `00bdd630` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdd634"></a> `00bdd634` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdd638"></a> `00bdd638` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdd63c"></a> `00bdd63c` | `15 fa 01 94` | bl 0x00c5be90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd640"></a> `00bdd640` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdd644"></a> `00bdd644` | `a0 00 00 b4` | cbz x0,0x00bdd658 | `CONDITIONAL_JUMP`
<a id="insn-00bdd648"></a> `00bdd648` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdd64c"></a> `00bdd64c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bdd650"></a> `00bdd650` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdd654"></a> `00bdd654` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdd658"></a> `00bdd658` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd65c"></a> `00bdd65c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd660"></a> `00bdd660` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdd664"></a> `00bdd664` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd5ec`](#insn-00bdd5ec) 範囲 `[['00bdd5ec', '00bdd647']]`
  - `CONDITIONAL_JUMP` [`00bdd644`](#insn-00bdd644) → [`00bdd658`](#insn-00bdd658)
  - `FALL_THROUGH` [`00bdd644`](#insn-00bdd644) → [`00bdd648`](#insn-00bdd648)
- ブロック [`00bdd648`](#insn-00bdd648) 範囲 `[['00bdd648', '00bdd657']]`
  - `FALL_THROUGH` [`00bdd654`](#insn-00bdd654) → [`00bdd658`](#insn-00bdd658)
- ブロック [`00bdd658`](#insn-00bdd658) 範囲 `[['00bdd658', '00bdd667']]`

## 命令位置別の参照

- [`00bdd5ec`](#insn-00bdd5ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5f0`](#insn-00bdd5f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5f4`](#insn-00bdd5f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd60c`](#insn-00bdd60c) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bdd620`](#insn-00bdd620) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bdd63c`](#insn-00bdd63c) → [`00c5be90`](../00c5b/00c5be90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be90` · 推定シンボル `None` · 推定型 `None`
- [`00bdd644`](#insn-00bdd644) → [`00bdd658`](#insn-00bdd658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd658`](#insn-00bdd658) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd65c`](#insn-00bdd65c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd5ec`](#insn-00bdd5ec)

~~~json
{
  "source": "00bdd5ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5f0`](#insn-00bdd5f0)

~~~json
{
  "source": "00bdd5f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5f4`](#insn-00bdd5f4)

~~~json
{
  "source": "00bdd5f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd60c`](#insn-00bdd60c)

~~~json
{
  "source": "00bdd60c",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd620`](#insn-00bdd620)

~~~json
{
  "source": "00bdd620",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd63c`](#insn-00bdd63c)

~~~json
{
  "source": "00bdd63c",
  "target": "00c5be90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd644`](#insn-00bdd644)

~~~json
{
  "source": "00bdd644",
  "target": "00bdd658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd658`](#insn-00bdd658)

~~~json
{
  "source": "00bdd658",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd65c`](#insn-00bdd65c)

~~~json
{
  "source": "00bdd65c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
