# 00bdbb6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdb744`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-8080cf5283f1710bd8775104cc6fbdc0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdbc08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-edcde6e52c0ebb00bf47ff2d9d12b466)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbb6c",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e98a4822ad9572cd130b4125dca121ce42f8de9e081d6c2bc2e2719212c1c84c",
  "source_text_sha256": "e98a4822ad9572cd130b4125dca121ce42f8de9e081d6c2bc2e2719212c1c84c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbb6c",
        "00bdbc0f"
      ]
    ],
    "bytes_sha256": "caf0cb993084d1cdff30f3a6cde41c2ce0296d96e66fc0fbf41b8e8251f3ffbc",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dde0](../00c5d/00c5dde0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5ddf0](../00c5d/00c5ddf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1111 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_
               (undefined8 param_1,undefined8 param_2,undefined4 param_3,undefined8 param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_58 [16];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _Znwm(0x138);
  _ZN8firebase4auth10AuthResultC2ERKS1_(uVar2,param_4);
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_58,param_2,param_3,uVar2,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv_00c9b9e8
            );
  _ZN8firebase12FutureHandleC1ERKS0_(param_1,auStack_58);
  _ZN8firebase12FutureHandleD2Ev(auStack_58);
                    /* try { // try from 00bdbbe8 to 00cdbbf7 has its CatchHandler @ 00bdeec4 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00bdbbf8 to 00cdc323 has its CatchHandler @ 00bd6f4c */
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
<a id="insn-00bdbb6c"></a> `00bdbb6c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdbb70"></a> `00bdbb70` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdbb74"></a> `00bdbb74` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdbb78"></a> `00bdbb78` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdbb7c"></a> `00bdbb7c` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdbb80"></a> `00bdbb80` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdbb84"></a> `00bdbb84` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdbb88"></a> `00bdbb88` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdbb8c"></a> `00bdbb8c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdbb90"></a> `00bdbb90` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdbb94"></a> `00bdbb94` | `00 27 80 52` | mov w0,#0x138 | `FALL_THROUGH`
<a id="insn-00bdbb98"></a> `00bdbb98` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bdbb9c"></a> `00bdbb9c` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bdbba0"></a> `00bdbba0` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdbba4"></a> `00bdbba4` | `bb f0 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbba8"></a> `00bdbba8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdbbac"></a> `00bdbbac` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdbbb0"></a> `00bdbbb0` | `90 08 02 94` | bl 0x00c5ddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbbb4"></a> `00bdbbb4` | `03 06 00 90` | adrp x3,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdbbb8"></a> `00bdbbb8` | `63 f4 44 f9` | ldr x3,[x3, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bdbbbc"></a> `00bdbbbc` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdbbc0"></a> `00bdbbc0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdbbc4"></a> `00bdbbc4` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bdbbc8"></a> `00bdbbc8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdbbcc"></a> `00bdbbcc` | `9d fc 01 94` | bl 0x00c5ae40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbbd0"></a> `00bdbbd0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdbbd4"></a> `00bdbbd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbbd8"></a> `00bdbbd8` | `8a fc 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbbdc"></a> `00bdbbdc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdbbe0"></a> `00bdbbe0` | `ac fb 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbbe4"></a> `00bdbbe4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdbbe8"></a> `00bdbbe8` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdbbec"></a> `00bdbbec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdbbf0"></a> `00bdbbf0` | `e1 00 00 54` | b.ne 0x00bdbc0c | `CONDITIONAL_JUMP`
<a id="insn-00bdbbf4"></a> `00bdbbf4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdbbf8"></a> `00bdbbf8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdbbfc"></a> `00bdbbfc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdbc00"></a> `00bdbc00` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdbc04"></a> `00bdbc04` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdbc08"></a> `00bdbc08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdbc0c"></a> `00bdbc0c` | `b5 f0 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbb6c`](#insn-00bdbb6c) 範囲 `[['00bdbb6c', '00bdbbe7']]`
  - `FALL_THROUGH` [`00bdbbe4`](#insn-00bdbbe4) → [`00bdbbe8`](#insn-00bdbbe8)
- ブロック [`00bdbbe8`](#insn-00bdbbe8) 範囲 `[['00bdbbe8', '00bdbbf3']]`
  - `CONDITIONAL_JUMP` [`00bdbbf0`](#insn-00bdbbf0) → [`00bdbc0c`](#insn-00bdbc0c)
  - `FALL_THROUGH` [`00bdbbf0`](#insn-00bdbbf0) → [`00bdbbf4`](#insn-00bdbbf4)
- ブロック [`00bdbbf4`](#insn-00bdbbf4) 範囲 `[['00bdbbf4', '00bdbbf7']]`
  - `FALL_THROUGH` [`00bdbbf4`](#insn-00bdbbf4) → [`00bdbbf8`](#insn-00bdbbf8)
- ブロック [`00bdbbf8`](#insn-00bdbbf8) 範囲 `[['00bdbbf8', '00bdbc0b']]`
- ブロック [`00bdbc0c`](#insn-00bdbc0c) 範囲 `[['00bdbc0c', '00bdbc0f']]`

## 命令位置別の参照

- [`00bdbb70`](#insn-00bdbb70) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbb74`](#insn-00bdbb74) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbb78`](#insn-00bdbb78) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbb7c`](#insn-00bdbb7c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbba0`](#insn-00bdbba0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbba4`](#insn-00bdbba4) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbb0`](#insn-00bdbbb0) → [`00c5ddf0`](../00c5d/00c5ddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ddf0` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbb8`](#insn-00bdbbb8) → `00c9b9e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbb8`](#insn-00bdbbb8) → [`00bcfcd8`](../00bcf/00bcfcd8.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfcd8` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv` · 推定型 `None`
- [`00bdbbcc`](#insn-00bdbbcc) → [`00c5ae40`](../00c5a/00c5ae40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae40` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbd8`](#insn-00bdbbd8) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbe0`](#insn-00bdbbe0) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbe8`](#insn-00bdbbe8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbf0`](#insn-00bdbbf0) → [`00bdbc0c`](#insn-00bdbc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbf4`](#insn-00bdbbf4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbf8`](#insn-00bdbbf8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbbfc`](#insn-00bdbbfc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbc00`](#insn-00bdbc00) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbc0c`](#insn-00bdbc0c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbb70`](#insn-00bdbb70)

~~~json
{
  "source": "00bdbb70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbb74`](#insn-00bdbb74)

~~~json
{
  "source": "00bdbb74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbb78`](#insn-00bdbb78)

~~~json
{
  "source": "00bdbb78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbb7c`](#insn-00bdbb7c)

~~~json
{
  "source": "00bdbb7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbba0`](#insn-00bdbba0)

~~~json
{
  "source": "00bdbba0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbba4`](#insn-00bdbba4)

~~~json
{
  "source": "00bdbba4",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbb0`](#insn-00bdbbb0)

~~~json
{
  "source": "00bdbbb0",
  "target": "00c5ddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbb8`](#insn-00bdbbb8)

~~~json
{
  "source": "00bdbbb8",
  "target": "00c9b9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbb8`](#insn-00bdbbb8)

~~~json
{
  "source": "00bdbbb8",
  "target": "00bcfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbcc`](#insn-00bdbbcc)

~~~json
{
  "source": "00bdbbcc",
  "target": "00c5ae40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbd8`](#insn-00bdbbd8)

~~~json
{
  "source": "00bdbbd8",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbe0`](#insn-00bdbbe0)

~~~json
{
  "source": "00bdbbe0",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbbe8`](#insn-00bdbbe8)

~~~json
{
  "source": "00bdbbe8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbbf0`](#insn-00bdbbf0)

~~~json
{
  "source": "00bdbbf0",
  "target": "00bdbc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbbf4`](#insn-00bdbbf4)

~~~json
{
  "source": "00bdbbf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbbf8`](#insn-00bdbbf8)

~~~json
{
  "source": "00bdbbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbbfc`](#insn-00bdbbfc)

~~~json
{
  "source": "00bdbbfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbc00`](#insn-00bdbc00)

~~~json
{
  "source": "00bdbc00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbc0c`](#insn-00bdbc0c)

~~~json
{
  "source": "00bdbc0c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
