# 00bfcc0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbc18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbc18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-5628f74b0d60089859e9d3af85444e34)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcc0c",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efd482e09240dcf09da7687dffb4afb9ee63a852910ba2bbb76fec77137ddb6f",
  "source_text_sha256": "efd482e09240dcf09da7687dffb4afb9ee63a852910ba2bbb76fec77137ddb6f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcc0c",
        "00bfcc87"
      ]
    ],
    "bytes_sha256": "7a03541f829605b18161199951a079ac60f39aeacdf9ba0410032c430d3672ad",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5f370](../00c5f/00c5f370.md)
- [00c5f3b0](../00c5f/00c5f3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 674 bytes

~~~c

long _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEE7copyfmtERKS3_(long param_1,long param_2)

{
  undefined4 uVar1;
  
  if (param_1 != param_2) {
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,0);
    _ZNSt6__ndk18ios_base7copyfmtERKS0_(param_1,param_2);
    uVar1 = *(undefined4 *)(param_2 + 0x90);
    *(undefined8 *)(param_1 + 0x88) = *(undefined8 *)(param_2 + 0x88);
    *(undefined4 *)(param_1 + 0x90) = uVar1;
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,2);
    *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x24);
    _ZNSt6__ndk18ios_base5clearEj(param_1,*(undefined4 *)(param_1 + 0x20));
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcc0c"></a> `00bfcc0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcc10"></a> `00bfcc10` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfcc14"></a> `00bfcc14` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcc18"></a> `00bfcc18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfcc1c"></a> `00bfcc1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcc20"></a> `00bfcc20` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bfcc24"></a> `00bfcc24` | `80 02 00 54` | b.eq 0x00bfcc74 | `CONDITIONAL_JUMP`
<a id="insn-00bfcc28"></a> `00bfcc28` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcc2c"></a> `00bfcc2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc30"></a> `00bfcc30` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bfcc34"></a> `00bfcc34` | `cf 89 01 94` | bl 0x00c5f370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc38"></a> `00bfcc38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc3c"></a> `00bfcc3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfcc40"></a> `00bfcc40` | `dc 89 01 94` | bl 0x00c5f3b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc44"></a> `00bfcc44` | `88 46 40 f9` | ldr x8,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfcc48"></a> `00bfcc48` | `89 92 40 b9` | ldr w9,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfcc4c"></a> `00bfcc4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc50"></a> `00bfcc50` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00bfcc54"></a> `00bfcc54` | `68 46 00 f9` | str x8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfcc58"></a> `00bfcc58` | `69 92 00 b9` | str w9,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfcc5c"></a> `00bfcc5c` | `c5 89 01 94` | bl 0x00c5f370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc60"></a> `00bfcc60` | `88 26 40 b9` | ldr w8,[x20, #0x24] | `FALL_THROUGH`
<a id="insn-00bfcc64"></a> `00bfcc64` | `61 22 40 b9` | ldr w1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcc68"></a> `00bfcc68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc6c"></a> `00bfcc6c` | `68 26 00 b9` | str w8,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00bfcc70"></a> `00bfcc70` | `b4 71 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc74"></a> `00bfcc74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc78"></a> `00bfcc78` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcc7c"></a> `00bfcc7c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfcc80"></a> `00bfcc80` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcc84"></a> `00bfcc84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcc0c`](#insn-00bfcc0c) 範囲 `[['00bfcc0c', '00bfcc27']]`
  - `CONDITIONAL_JUMP` [`00bfcc24`](#insn-00bfcc24) → [`00bfcc74`](#insn-00bfcc74)
  - `FALL_THROUGH` [`00bfcc24`](#insn-00bfcc24) → [`00bfcc28`](#insn-00bfcc28)
- ブロック [`00bfcc28`](#insn-00bfcc28) 範囲 `[['00bfcc28', '00bfcc73']]`
  - `FALL_THROUGH` [`00bfcc70`](#insn-00bfcc70) → [`00bfcc74`](#insn-00bfcc74)
- ブロック [`00bfcc74`](#insn-00bfcc74) 範囲 `[['00bfcc74', '00bfcc87']]`

## 命令位置別の参照

- [`00bfcc10`](#insn-00bfcc10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc14`](#insn-00bfcc14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc24`](#insn-00bfcc24) → [`00bfcc74`](#insn-00bfcc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc34`](#insn-00bfcc34) → [`00c5f370`](../00c5f/00c5f370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f370` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc40`](#insn-00bfcc40) → [`00c5f3b0`](../00c5f/00c5f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc5c`](#insn-00bfcc5c) → [`00c5f370`](../00c5f/00c5f370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f370` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc70`](#insn-00bfcc70) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc78`](#insn-00bfcc78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc7c`](#insn-00bfcc7c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcc10`](#insn-00bfcc10)

~~~json
{
  "source": "00bfcc10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc14`](#insn-00bfcc14)

~~~json
{
  "source": "00bfcc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc24`](#insn-00bfcc24)

~~~json
{
  "source": "00bfcc24",
  "target": "00bfcc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc34`](#insn-00bfcc34)

~~~json
{
  "source": "00bfcc34",
  "target": "00c5f370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc40`](#insn-00bfcc40)

~~~json
{
  "source": "00bfcc40",
  "target": "00c5f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc5c`](#insn-00bfcc5c)

~~~json
{
  "source": "00bfcc5c",
  "target": "00c5f370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc70`](#insn-00bfcc70)

~~~json
{
  "source": "00bfcc70",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc78`](#insn-00bfcc78)

~~~json
{
  "source": "00bfcc78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc7c`](#insn-00bfcc7c)

~~~json
{
  "source": "00bfcc7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
