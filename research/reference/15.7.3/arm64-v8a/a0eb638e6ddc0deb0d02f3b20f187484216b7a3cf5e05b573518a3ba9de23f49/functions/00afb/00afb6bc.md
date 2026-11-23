# 00afb6bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afb5f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb5f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-0218e479a15878e0beea8e9adfbd44fc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb700`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb700.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-956737b9ad3b6db5f49b705aed2f12ca)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb6bc",
  "name": "_ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f2a0e09251b25d8dde5c5af4d102d3669284e1ef63decdc2b279fe7e95bd512",
  "source_text_sha256": "2f2a0e09251b25d8dde5c5af4d102d3669284e1ef63decdc2b279fe7e95bd512",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb6bc",
        "00afb753"
      ]
    ],
    "bytes_sha256": "43566a7c083485cc76417b1ec5aa970d818dcaeecdbdf6538281edd65735216e",
    "instruction_count": 38,
    "instruction_bytes": 152,
    "body_bytes": 152,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1351 bytes

~~~c

void _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list
               (long param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  long local_38;
  
                    /* try { // try from 00afb6c4 to 00bfb6db has its CatchHandler @ 00aff468 */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar7 = param_4[1];
  uVar6 = *param_4;
  uVar5 = param_4[3];
  uVar4 = param_4[2];
  plVar3 = *(long **)(param_1 + 8);
                    /* try { // try from 00afb6ec to 00bfb6f3 has its CatchHandler @ 00aff464 */
  iVar2 = (**(code **)(*plVar3 + 0x18))(plVar3);
  if (iVar2 <= param_2) {
                    /* try { // try from 00afb71c to 00bfb72f has its CatchHandler @ 00aff460 */
    local_60 = uVar6;
    uStack_58 = uVar7;
    uStack_50 = uVar4;
    uStack_48 = uVar5;
    (**(code **)(*plVar3 + 0x20))(plVar3,param_2,param_3,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00afb740 to 00bfb757 has its CatchHandler @ 00b0037c */
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
<a id="insn-00afb6bc"></a> `00afb6bc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afb6c0"></a> `00afb6c0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afb6c4"></a> `00afb6c4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb6c8"></a> `00afb6c8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afb6cc"></a> `00afb6cc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afb6d0"></a> `00afb6d0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afb6d4"></a> `00afb6d4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb6d8"></a> `00afb6d8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00afb6dc"></a> `00afb6dc` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00afb6e0"></a> `00afb6e0` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb6e4"></a> `00afb6e4` | `61 00 40 ad` | ldp q1,q0,[x3] | `FALL_THROUGH`
<a id="insn-00afb6e8"></a> `00afb6e8` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afb6ec"></a> `00afb6ec` | `e1 03 00 ad` | stp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00afb6f0"></a> `00afb6f0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00afb6f4"></a> `00afb6f4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afb6f8"></a> `00afb6f8` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afb6fc"></a> `00afb6fc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb700"></a> `00afb700` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00afb704"></a> `00afb704` | `4c 01 00 54` | b.gt 0x00afb72c | `CONDITIONAL_JUMP`
<a id="insn-00afb708"></a> `00afb708` | `e0 07 40 ad` | ldp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00afb70c"></a> `00afb70c` | `e3 83 00 91` | add x3,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afb710"></a> `00afb710` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afb714"></a> `00afb714` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afb718"></a> `00afb718` | `e0 07 01 ad` | stp q0,q1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb71c"></a> `00afb71c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00afb720"></a> `00afb720` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00afb724"></a> `00afb724` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afb728"></a> `00afb728` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb72c"></a> `00afb72c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb730"></a> `00afb730` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb734"></a> `00afb734` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afb738"></a> `00afb738` | `c1 00 00 54` | b.ne 0x00afb750 | `CONDITIONAL_JUMP`
<a id="insn-00afb73c"></a> `00afb73c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afb740"></a> `00afb740` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb744"></a> `00afb744` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afb748"></a> `00afb748` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afb74c"></a> `00afb74c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afb750"></a> `00afb750` | `3c 7e 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb6bc`](#insn-00afb6bc) 範囲 `[['00afb6bc', '00afb6c3']]`
  - `FALL_THROUGH` [`00afb6c0`](#insn-00afb6c0) → [`00afb6c4`](#insn-00afb6c4)
- ブロック [`00afb6c4`](#insn-00afb6c4) 範囲 `[['00afb6c4', '00afb6eb']]`
  - `FALL_THROUGH` [`00afb6e8`](#insn-00afb6e8) → [`00afb6ec`](#insn-00afb6ec)
- ブロック [`00afb6ec`](#insn-00afb6ec) 範囲 `[['00afb6ec', '00afb707']]`
  - `CONDITIONAL_JUMP` [`00afb704`](#insn-00afb704) → [`00afb72c`](#insn-00afb72c)
  - `FALL_THROUGH` [`00afb704`](#insn-00afb704) → [`00afb708`](#insn-00afb708)
- ブロック [`00afb708`](#insn-00afb708) 範囲 `[['00afb708', '00afb71b']]`
  - `FALL_THROUGH` [`00afb718`](#insn-00afb718) → [`00afb71c`](#insn-00afb71c)
- ブロック [`00afb71c`](#insn-00afb71c) 範囲 `[['00afb71c', '00afb72b']]`
  - `FALL_THROUGH` [`00afb728`](#insn-00afb728) → [`00afb72c`](#insn-00afb72c)
- ブロック [`00afb72c`](#insn-00afb72c) 範囲 `[['00afb72c', '00afb73b']]`
  - `CONDITIONAL_JUMP` [`00afb738`](#insn-00afb738) → [`00afb750`](#insn-00afb750)
  - `FALL_THROUGH` [`00afb738`](#insn-00afb738) → [`00afb73c`](#insn-00afb73c)
- ブロック [`00afb73c`](#insn-00afb73c) 範囲 `[['00afb73c', '00afb73f']]`
  - `FALL_THROUGH` [`00afb73c`](#insn-00afb73c) → [`00afb740`](#insn-00afb740)
- ブロック [`00afb740`](#insn-00afb740) 範囲 `[['00afb740', '00afb74f']]`
- ブロック [`00afb750`](#insn-00afb750) 範囲 `[['00afb750', '00afb753']]`

## 命令位置別の参照

- [`00afb6c0`](#insn-00afb6c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6c4`](#insn-00afb6c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6c8`](#insn-00afb6c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6e0`](#insn-00afb6e0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6ec`](#insn-00afb6ec) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb704`](#insn-00afb704) → [`00afb72c`](#insn-00afb72c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb708`](#insn-00afb708) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb718`](#insn-00afb718) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb730`](#insn-00afb730) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb738`](#insn-00afb738) → [`00afb750`](#insn-00afb750) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb73c`](#insn-00afb73c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb740`](#insn-00afb740) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb744`](#insn-00afb744) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb750`](#insn-00afb750) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb6c0`](#insn-00afb6c0)

~~~json
{
  "source": "00afb6c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6c4`](#insn-00afb6c4)

~~~json
{
  "source": "00afb6c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6c8`](#insn-00afb6c8)

~~~json
{
  "source": "00afb6c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6e0`](#insn-00afb6e0)

~~~json
{
  "source": "00afb6e0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6ec`](#insn-00afb6ec)

~~~json
{
  "source": "00afb6ec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb704`](#insn-00afb704)

~~~json
{
  "source": "00afb704",
  "target": "00afb72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb708`](#insn-00afb708)

~~~json
{
  "source": "00afb708",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb718`](#insn-00afb718)

~~~json
{
  "source": "00afb718",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb730`](#insn-00afb730)

~~~json
{
  "source": "00afb730",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb738`](#insn-00afb738)

~~~json
{
  "source": "00afb738",
  "target": "00afb750",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb73c`](#insn-00afb73c)

~~~json
{
  "source": "00afb73c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb740`](#insn-00afb740)

~~~json
{
  "source": "00afb740",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb744`](#insn-00afb744)

~~~json
{
  "source": "00afb744",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb750`](#insn-00afb750)

~~~json
{
  "source": "00afb750",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
