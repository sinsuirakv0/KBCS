# 00afb5ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afb5a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb5a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f29ca06f9be7f6ca5e853fd75979c761)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5b370`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b370.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-8dc0b2c26079ffd92dbaeacab58d3b6b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb5ec",
  "name": "_ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769",
  "source_text_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb5ec",
        "00afb67f"
      ]
    ],
    "bytes_sha256": "2843920219133e2b3332d63935a1bec5fc4d9335f7c5c88072d6513b74934313",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1201 bytes

~~~c

void _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list
               (long *param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar6 = param_4[1];
  uVar5 = *param_4;
                    /* try { // try from 00afb618 to 00bfb61f has its CatchHandler @ 00aff4c0 */
  uVar4 = param_4[3];
  uVar3 = param_4[2];
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
                    /* try { // try from 00afb648 to 00bfb65f has its CatchHandler @ 00aff4bc */
    local_60 = uVar5;
    uStack_58 = uVar6;
    uStack_50 = uVar3;
    uStack_48 = uVar4;
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00afb670 to 00bfb677 has its CatchHandler @ 00aff4b8 */
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
<a id="insn-00afb5ec"></a> `00afb5ec` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afb5f0"></a> `00afb5f0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afb5f4"></a> `00afb5f4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb5f8"></a> `00afb5f8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afb5fc"></a> `00afb5fc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afb600"></a> `00afb600` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afb604"></a> `00afb604` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb608"></a> `00afb608` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00afb60c"></a> `00afb60c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afb610"></a> `00afb610` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00afb614"></a> `00afb614` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb618"></a> `00afb618` | `61 00 40 ad` | ldp q1,q0,[x3] | `FALL_THROUGH`
<a id="insn-00afb61c"></a> `00afb61c` | `e1 03 00 ad` | stp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00afb620"></a> `00afb620` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afb624"></a> `00afb624` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afb628"></a> `00afb628` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb62c"></a> `00afb62c` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00afb630"></a> `00afb630` | `4c 01 00 54` | b.gt 0x00afb658 | `CONDITIONAL_JUMP`
<a id="insn-00afb634"></a> `00afb634` | `e0 07 40 ad` | ldp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00afb638"></a> `00afb638` | `e3 83 00 91` | add x3,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afb63c"></a> `00afb63c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afb640"></a> `00afb640` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afb644"></a> `00afb644` | `e0 07 01 ad` | stp q0,q1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb648"></a> `00afb648` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00afb64c"></a> `00afb64c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00afb650"></a> `00afb650` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afb654"></a> `00afb654` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb658"></a> `00afb658` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb65c"></a> `00afb65c` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb660"></a> `00afb660` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afb664"></a> `00afb664` | `c1 00 00 54` | b.ne 0x00afb67c | `CONDITIONAL_JUMP`
<a id="insn-00afb668"></a> `00afb668` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afb66c"></a> `00afb66c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb670"></a> `00afb670` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afb674"></a> `00afb674` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afb678"></a> `00afb678` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afb67c"></a> `00afb67c` | `85 7e 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb5ec`](#insn-00afb5ec) 範囲 `[['00afb5ec', '00afb617']]`
  - `FALL_THROUGH` [`00afb614`](#insn-00afb614) → [`00afb618`](#insn-00afb618)
- ブロック [`00afb618`](#insn-00afb618) 範囲 `[['00afb618', '00afb633']]`
  - `CONDITIONAL_JUMP` [`00afb630`](#insn-00afb630) → [`00afb658`](#insn-00afb658)
  - `FALL_THROUGH` [`00afb630`](#insn-00afb630) → [`00afb634`](#insn-00afb634)
- ブロック [`00afb634`](#insn-00afb634) 範囲 `[['00afb634', '00afb647']]`
  - `FALL_THROUGH` [`00afb644`](#insn-00afb644) → [`00afb648`](#insn-00afb648)
- ブロック [`00afb648`](#insn-00afb648) 範囲 `[['00afb648', '00afb657']]`
  - `FALL_THROUGH` [`00afb654`](#insn-00afb654) → [`00afb658`](#insn-00afb658)
- ブロック [`00afb658`](#insn-00afb658) 範囲 `[['00afb658', '00afb667']]`
  - `CONDITIONAL_JUMP` [`00afb664`](#insn-00afb664) → [`00afb67c`](#insn-00afb67c)
  - `FALL_THROUGH` [`00afb664`](#insn-00afb664) → [`00afb668`](#insn-00afb668)
- ブロック [`00afb668`](#insn-00afb668) 範囲 `[['00afb668', '00afb66f']]`
  - `FALL_THROUGH` [`00afb66c`](#insn-00afb66c) → [`00afb670`](#insn-00afb670)
- ブロック [`00afb670`](#insn-00afb670) 範囲 `[['00afb670', '00afb67b']]`
- ブロック [`00afb67c`](#insn-00afb67c) 範囲 `[['00afb67c', '00afb67f']]`

## 命令位置別の参照

- [`00afb5f0`](#insn-00afb5f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5f4`](#insn-00afb5f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5f8`](#insn-00afb5f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb614`](#insn-00afb614) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb61c`](#insn-00afb61c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb630`](#insn-00afb630) → [`00afb658`](#insn-00afb658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb634`](#insn-00afb634) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb644`](#insn-00afb644) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb65c`](#insn-00afb65c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb664`](#insn-00afb664) → [`00afb67c`](#insn-00afb67c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb668`](#insn-00afb668) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb66c`](#insn-00afb66c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb670`](#insn-00afb670) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb67c`](#insn-00afb67c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb5f0`](#insn-00afb5f0)

~~~json
{
  "source": "00afb5f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5f4`](#insn-00afb5f4)

~~~json
{
  "source": "00afb5f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5f8`](#insn-00afb5f8)

~~~json
{
  "source": "00afb5f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb614`](#insn-00afb614)

~~~json
{
  "source": "00afb614",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb61c`](#insn-00afb61c)

~~~json
{
  "source": "00afb61c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb630`](#insn-00afb630)

~~~json
{
  "source": "00afb630",
  "target": "00afb658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb634`](#insn-00afb634)

~~~json
{
  "source": "00afb634",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb644`](#insn-00afb644)

~~~json
{
  "source": "00afb644",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb65c`](#insn-00afb65c)

~~~json
{
  "source": "00afb65c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb664`](#insn-00afb664)

~~~json
{
  "source": "00afb664",
  "target": "00afb67c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb668`](#insn-00afb668)

~~~json
{
  "source": "00afb668",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb66c`](#insn-00afb66c)

~~~json
{
  "source": "00afb66c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb670`](#insn-00afb670)

~~~json
{
  "source": "00afb670",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb67c`](#insn-00afb67c)

~~~json
{
  "source": "00afb67c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
