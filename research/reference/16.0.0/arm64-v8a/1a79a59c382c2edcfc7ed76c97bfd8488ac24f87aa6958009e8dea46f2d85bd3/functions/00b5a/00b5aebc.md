# 00b5aebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb138`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb138.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-11235ecc95839b53ee3b99d930fc6a16)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5b2e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b2e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0008.md#compare-6f948365b94d1c889b50db071818dbc1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5aebc",
  "name": "_ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b12e40e55e0bae70cda92cdd48c75d9a489ce9dbe3cfec071e7830de9d594cd4",
  "source_text_sha256": "b12e40e55e0bae70cda92cdd48c75d9a489ce9dbe3cfec071e7830de9d594cd4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5aebc",
        "00b5af53"
      ]
    ],
    "bytes_sha256": "90c5058f0b3fd96bb2a5ac800cd82e34331859216c81d71826965504608135ba",
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

- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 768 bytes

~~~c

void _ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list
               (long *param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  undefined8 local_70;
  undefined8 uStack_68;
  undefined8 uStack_60;
  undefined8 uStack_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
    uStack_68 = param_4[1];
    local_70 = *param_4;
    uStack_58 = param_4[3];
    uStack_60 = param_4[2];
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_70);
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
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
<a id="insn-00b5aebc"></a> `00b5aebc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b5aec0"></a> `00b5aec0` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5aec4"></a> `00b5aec4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5aec8"></a> `00b5aec8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5aecc"></a> `00b5aecc` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b5aed0"></a> `00b5aed0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b5aed4"></a> `00b5aed4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5aed8"></a> `00b5aed8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b5aedc"></a> `00b5aedc` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00b5aee0"></a> `00b5aee0` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b5aee4"></a> `00b5aee4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5aee8"></a> `00b5aee8` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b5aeec"></a> `00b5aeec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5aef0"></a> `00b5aef0` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00b5aef4"></a> `00b5aef4` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5aef8"></a> `00b5aef8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5aefc"></a> `00b5aefc` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00b5af00"></a> `00b5af00` | `4c 01 00 54` | b.gt 0x00b5af28 | `CONDITIONAL_JUMP`
<a id="insn-00b5af04"></a> `00b5af04` | `c1 02 40 ad` | ldp q1,q0,[x22] | `FALL_THROUGH`
<a id="insn-00b5af08"></a> `00b5af08` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00b5af0c"></a> `00b5af0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5af10"></a> `00b5af10` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00b5af14"></a> `00b5af14` | `e1 03 00 ad` | stp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00b5af18"></a> `00b5af18` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5af1c"></a> `00b5af1c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00b5af20"></a> `00b5af20` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5af24"></a> `00b5af24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5af28"></a> `00b5af28` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b5af2c"></a> `00b5af2c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b5af30"></a> `00b5af30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5af34"></a> `00b5af34` | `e1 00 00 54` | b.ne 0x00b5af50 | `CONDITIONAL_JUMP`
<a id="insn-00b5af38"></a> `00b5af38` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b5af3c"></a> `00b5af3c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5af40"></a> `00b5af40` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5af44"></a> `00b5af44` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5af48"></a> `00b5af48` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b5af4c"></a> `00b5af4c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5af50"></a> `00b5af50` | `e4 f2 03 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5aebc`](#insn-00b5aebc) 範囲 `[['00b5aebc', '00b5af03']]`
  - `CONDITIONAL_JUMP` [`00b5af00`](#insn-00b5af00) → [`00b5af28`](#insn-00b5af28)
  - `FALL_THROUGH` [`00b5af00`](#insn-00b5af00) → [`00b5af04`](#insn-00b5af04)
- ブロック [`00b5af04`](#insn-00b5af04) 範囲 `[['00b5af04', '00b5af27']]`
  - `FALL_THROUGH` [`00b5af24`](#insn-00b5af24) → [`00b5af28`](#insn-00b5af28)
- ブロック [`00b5af28`](#insn-00b5af28) 範囲 `[['00b5af28', '00b5af37']]`
  - `CONDITIONAL_JUMP` [`00b5af34`](#insn-00b5af34) → [`00b5af50`](#insn-00b5af50)
  - `FALL_THROUGH` [`00b5af34`](#insn-00b5af34) → [`00b5af38`](#insn-00b5af38)
- ブロック [`00b5af38`](#insn-00b5af38) 範囲 `[['00b5af38', '00b5af4f']]`
- ブロック [`00b5af50`](#insn-00b5af50) 範囲 `[['00b5af50', '00b5af53']]`

## 命令位置別の参照

- [`00b5aec0`](#insn-00b5aec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aec4`](#insn-00b5aec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aec8`](#insn-00b5aec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aecc`](#insn-00b5aecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aee8`](#insn-00b5aee8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af00`](#insn-00b5af00) → [`00b5af28`](#insn-00b5af28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af14`](#insn-00b5af14) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af2c`](#insn-00b5af2c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af34`](#insn-00b5af34) → [`00b5af50`](#insn-00b5af50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af38`](#insn-00b5af38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af3c`](#insn-00b5af3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af40`](#insn-00b5af40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af44`](#insn-00b5af44) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5af50`](#insn-00b5af50) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5aec0`](#insn-00b5aec0)

~~~json
{
  "source": "00b5aec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aec4`](#insn-00b5aec4)

~~~json
{
  "source": "00b5aec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aec8`](#insn-00b5aec8)

~~~json
{
  "source": "00b5aec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aecc`](#insn-00b5aecc)

~~~json
{
  "source": "00b5aecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aee8`](#insn-00b5aee8)

~~~json
{
  "source": "00b5aee8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af00`](#insn-00b5af00)

~~~json
{
  "source": "00b5af00",
  "target": "00b5af28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af14`](#insn-00b5af14)

~~~json
{
  "source": "00b5af14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af2c`](#insn-00b5af2c)

~~~json
{
  "source": "00b5af2c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af34`](#insn-00b5af34)

~~~json
{
  "source": "00b5af34",
  "target": "00b5af50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af38`](#insn-00b5af38)

~~~json
{
  "source": "00b5af38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af3c`](#insn-00b5af3c)

~~~json
{
  "source": "00b5af3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af40`](#insn-00b5af40)

~~~json
{
  "source": "00b5af40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af44`](#insn-00b5af44)

~~~json
{
  "source": "00b5af44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5af50`](#insn-00b5af50)

~~~json
{
  "source": "00b5af50",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
