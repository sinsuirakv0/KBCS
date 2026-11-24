# 00bfec8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdc98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-857659d83d64f3f0997581b718e12887)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfec8c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e46543673319600f24eaf07630290dc6a496673e065d95d3c703076c96601e3",
  "source_text_sha256": "0e46543673319600f24eaf07630290dc6a496673e065d95d3c703076c96601e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfec8c",
        "00bfed1b"
      ]
    ],
    "bytes_sha256": "60ab207b9585ce9147af6bce21b0b8df6e0c8263447c84369b5420c891e8f56a",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c5f430](../00c5f/00c5f430.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 644 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  undefined4 uVar1;
  long *plVar2;
  undefined1 auStack_38 [8];
  
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9bcd0);
  uVar1 = (**(code **)(*plVar2 + 0x38))(plVar2,10);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc(param_1,param_2,param_3,uVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfec8c"></a> `00bfec8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfec90"></a> `00bfec90` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfec94"></a> `00bfec94` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfec98"></a> `00bfec98` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfec9c"></a> `00bfec9c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeca0"></a> `00bfeca0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfeca4"></a> `00bfeca4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfeca8"></a> `00bfeca8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfecac"></a> `00bfecac` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bfecb0"></a> `00bfecb0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfecb4"></a> `00bfecb4` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfecb8"></a> `00bfecb8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfecbc"></a> `00bfecbc` | `00 00 09 8b` | add x0,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfecc0"></a> `00bfecc0` | `94 69 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecc4"></a> `00bfecc4` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfecc8"></a> `00bfecc8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeccc"></a> `00bfeccc` | `21 68 46 f9` | ldr x1,[x1, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bfecd0"></a> `00bfecd0` | `94 69 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecd4"></a> `00bfecd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfecd8"></a> `00bfecd8` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfecdc"></a> `00bfecdc` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00bfece0"></a> `00bfece0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfece4"></a> `00bfece4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bfece8"></a> `00bfece8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfecec"></a> `00bfecec` | `91 69 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecf0"></a> `00bfecf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfecf4"></a> `00bfecf4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bfecf8"></a> `00bfecf8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bfecfc"></a> `00bfecfc` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00bfed00"></a> `00bfed00` | `cc 81 01 94` | bl 0x00c5f430 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed04"></a> `00bfed04` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfed08"></a> `00bfed08` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfed0c"></a> `00bfed0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfed10"></a> `00bfed10` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfed14"></a> `00bfed14` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfed18"></a> `00bfed18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfec8c`](#insn-00bfec8c) 範囲 `[['00bfec8c', '00bfed1b']]`

## 命令位置別の参照

- [`00bfec94`](#insn-00bfec94) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec98`](#insn-00bfec98) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec9c`](#insn-00bfec9c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfecc0`](#insn-00bfecc0) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bfeccc`](#insn-00bfeccc) → `00c9bcd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfeccc`](#insn-00bfeccc) → `01128ed8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfecd0`](#insn-00bfecd0) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bfecec`](#insn-00bfecec) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bfed00`](#insn-00bfed00) → [`00c5f430`](../00c5f/00c5f430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f430` · 推定シンボル `None` · 推定型 `None`
- [`00bfed04`](#insn-00bfed04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed08`](#insn-00bfed08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed0c`](#insn-00bfed0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfec94`](#insn-00bfec94)

~~~json
{
  "source": "00bfec94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec98`](#insn-00bfec98)

~~~json
{
  "source": "00bfec98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec9c`](#insn-00bfec9c)

~~~json
{
  "source": "00bfec9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfecc0`](#insn-00bfecc0)

~~~json
{
  "source": "00bfecc0",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeccc`](#insn-00bfeccc)

~~~json
{
  "source": "00bfeccc",
  "target": "00c9bcd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bcd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfeccc`](#insn-00bfeccc)

~~~json
{
  "source": "00bfeccc",
  "target": "01128ed8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128ed8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfecd0`](#insn-00bfecd0)

~~~json
{
  "source": "00bfecd0",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfecec`](#insn-00bfecec)

~~~json
{
  "source": "00bfecec",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed00`](#insn-00bfed00)

~~~json
{
  "source": "00bfed00",
  "target": "00c5f430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed04`](#insn-00bfed04)

~~~json
{
  "source": "00bfed04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed08`](#insn-00bfed08)

~~~json
{
  "source": "00bfed08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed0c`](#insn-00bfed0c)

~~~json
{
  "source": "00bfed0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
