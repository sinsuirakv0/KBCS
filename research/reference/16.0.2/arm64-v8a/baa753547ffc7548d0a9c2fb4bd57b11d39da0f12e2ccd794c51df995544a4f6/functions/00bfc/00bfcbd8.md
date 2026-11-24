# 00bfcbd8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfcb3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-6e95aed9031f95399bbf68f33879725e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfdbcc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfdbcc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-8c6200ca45d69364fdd6345b6c8818d6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcbd8",
  "name": "FUN_00bfcbd8",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d995be51563684b231b4154ed21656baee3503e2023dadc79f33e796e6fb9661",
  "source_text_sha256": "d995be51563684b231b4154ed21656baee3503e2023dadc79f33e796e6fb9661",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcbd8",
        "00bfcc97"
      ]
    ],
    "bytes_sha256": "26628f46484eb15719b95981bee509e69fc0a975be59ce523bef6c5f891f8944",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcbd0](../00bfc/00bfcbd0.md)

## 呼び出し先

- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfcbd8(long *param_1,undefined8 param_2)

{
  long lVar1;
  long *plVar2;
  undefined1 auStack_30 [8];
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_30,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_30,
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9bbe0
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x38))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
    _ZNSt6__ndk16localeD1Ev(auStack_30);
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcbd8"></a> `00bfcbd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcbdc"></a> `00bfcbdc` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcbe0"></a> `00bfcbe0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcbe4"></a> `00bfcbe4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcbe8"></a> `00bfcbe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcbec"></a> `00bfcbec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcbf0"></a> `00bfcbf0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcbf4"></a> `00bfcbf4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcbf8"></a> `00bfcbf8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcbfc"></a> `00bfcbfc` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcc00"></a> `00bfcc00` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcc04"></a> `00bfcc04` | `a7 74 01 94` | bl 0x00c59ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc08"></a> `00bfcc08` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcc0c"></a> `00bfcc0c` | `a8 03 00 34` | cbz w8,0x00bfcc80 | `CONDITIONAL_JUMP`
<a id="insn-00bfcc10"></a> `00bfcc10` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc14"></a> `00bfcc14` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc18"></a> `00bfcc18` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcc1c"></a> `00bfcc1c` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcc20"></a> `00bfcc20` | `c8 6d 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc24"></a> `00bfcc24` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcc28"></a> `00bfcc28` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcc2c"></a> `00bfcc2c` | `21 f0 45 f9` | ldr x1,[x1, #0xbe0] | `FALL_THROUGH`
<a id="insn-00bfcc30"></a> `00bfcc30` | `c8 6d 01 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc34"></a> `00bfcc34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc38"></a> `00bfcc38` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfcc3c"></a> `00bfcc3c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc40"></a> `00bfcc40` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcc44"></a> `00bfcc44` | `28 1d 40 f9` | ldr x8,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-00bfcc48"></a> `00bfcc48` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcc4c"></a> `00bfcc4c` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcc50"></a> `00bfcc50` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfcc54"></a> `00bfcc54` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfcc58"></a> `00bfcc58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfcc5c"></a> `00bfcc5c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcc60"></a> `00bfcc60` | `c0 6d 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc64"></a> `00bfcc64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcc68"></a> `00bfcc68` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcc6c"></a> `00bfcc6c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcc70"></a> `00bfcc70` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcc74"></a> `00bfcc74` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcc78"></a> `00bfcc78` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfcc7c"></a> `00bfcc7c` | `bd 6d 01 94` | bl 0x00c58370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcc80"></a> `00bfcc80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcc84"></a> `00bfcc84` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcc88"></a> `00bfcc88` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcc8c"></a> `00bfcc8c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcc90"></a> `00bfcc90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcc94"></a> `00bfcc94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcbd8`](#insn-00bfcbd8) 範囲 `[['00bfcbd8', '00bfcc0f']]`
  - `CONDITIONAL_JUMP` [`00bfcc0c`](#insn-00bfcc0c) → [`00bfcc80`](#insn-00bfcc80)
  - `FALL_THROUGH` [`00bfcc0c`](#insn-00bfcc0c) → [`00bfcc10`](#insn-00bfcc10)
- ブロック [`00bfcc10`](#insn-00bfcc10) 範囲 `[['00bfcc10', '00bfcc7f']]`
  - `FALL_THROUGH` [`00bfcc7c`](#insn-00bfcc7c) → [`00bfcc80`](#insn-00bfcc80)
- ブロック [`00bfcc80`](#insn-00bfcc80) 範囲 `[['00bfcc80', '00bfcc97']]`

## 命令位置別の参照

- [`00bfcbe0`](#insn-00bfcbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbe4`](#insn-00bfcbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc00`](#insn-00bfcc00) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc04`](#insn-00bfcc04) → [`00c59ea0`](../00c59/00c59ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc08`](#insn-00bfcc08) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc0c`](#insn-00bfcc0c) → [`00bfcc80`](#insn-00bfcc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc20`](#insn-00bfcc20) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc2c`](#insn-00bfcc2c) → `00c9bbe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcc2c`](#insn-00bfcc2c) → `01127c78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcc30`](#insn-00bfcc30) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc60`](#insn-00bfcc60) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc70`](#insn-00bfcc70) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc7c`](#insn-00bfcc7c) → [`00c58370`](../00c58/00c58370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58370` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc84`](#insn-00bfcc84) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcc88`](#insn-00bfcc88) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcbe0`](#insn-00bfcbe0)

~~~json
{
  "source": "00bfcbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcbe4`](#insn-00bfcbe4)

~~~json
{
  "source": "00bfcbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc00`](#insn-00bfcc00)

~~~json
{
  "source": "00bfcc00",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc04`](#insn-00bfcc04)

~~~json
{
  "source": "00bfcc04",
  "target": "00c59ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc08`](#insn-00bfcc08)

~~~json
{
  "source": "00bfcc08",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc0c`](#insn-00bfcc0c)

~~~json
{
  "source": "00bfcc0c",
  "target": "00bfcc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc20`](#insn-00bfcc20)

~~~json
{
  "source": "00bfcc20",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc2c`](#insn-00bfcc2c)

~~~json
{
  "source": "00bfcc2c",
  "target": "00c9bbe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfcc2c`](#insn-00bfcc2c)

~~~json
{
  "source": "00bfcc2c",
  "target": "01127c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfcc30`](#insn-00bfcc30)

~~~json
{
  "source": "00bfcc30",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc60`](#insn-00bfcc60)

~~~json
{
  "source": "00bfcc60",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc70`](#insn-00bfcc70)

~~~json
{
  "source": "00bfcc70",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc7c`](#insn-00bfcc7c)

~~~json
{
  "source": "00bfcc7c",
  "target": "00c58370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcc84`](#insn-00bfcc84)

~~~json
{
  "source": "00bfcc84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcc88`](#insn-00bfcc88)

~~~json
{
  "source": "00bfcc88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
