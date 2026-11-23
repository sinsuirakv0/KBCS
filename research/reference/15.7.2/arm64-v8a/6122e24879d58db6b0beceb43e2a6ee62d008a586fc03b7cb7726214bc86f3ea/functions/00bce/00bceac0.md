# 00bceac0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bceb88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceb88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-4be8cbd3f220ee67074a89b1bb2566ac)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceac0",
  "name": "FUN_00bceac0",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "467df95cfcb92fde41417ccaa0c53b4a26c8d95e447a61942a17b5e08054e729",
  "source_text_sha256": "467df95cfcb92fde41417ccaa0c53b4a26c8d95e447a61942a17b5e08054e729",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceac0",
        "00bcebc3"
      ]
    ],
    "bytes_sha256": "8d3d3ac7e8842b1efcd7390f7045bc84dc6421c03f2f49bac8f67741656a03b0",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1256 bytes

~~~c

void FUN_00bceac0(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 2U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e2;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined2 *)((long)__ptr + lVar2) = 0x3a3a;
  plVar3 = *(long **)(param_1 + 0x18);
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 2;
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bcebbc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceac0"></a> `00bceac0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bceac4"></a> `00bceac4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bceac8"></a> `00bceac8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bceacc"></a> `00bceacc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcead0"></a> `00bcead0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcead4"></a> `00bcead4` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcead8"></a> `00bcead8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bceadc"></a> `00bceadc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bceae0"></a> `00bceae0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bceae4"></a> `00bceae4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bceae8"></a> `00bceae8` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bceaec"></a> `00bceaec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceaf0"></a> `00bceaf0` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bceaf4"></a> `00bceaf4` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bceaf8"></a> `00bceaf8` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bceafc"></a> `00bceafc` | `c0 00 00 54` | b.eq 0x00bceb14 | `CONDITIONAL_JUMP`
<a id="insn-00bceb00"></a> `00bceb00` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bceb04"></a> `00bceb04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bceb08"></a> `00bceb08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bceb0c"></a> `00bceb0c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bceb10"></a> `00bceb10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceb14"></a> `00bceb14` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bceb18"></a> `00bceb18` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bceb1c"></a> `00bceb1c` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bceb20"></a> `00bceb20` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bceb24"></a> `00bceb24` | `49 01 00 54` | b.ls 0x00bceb4c | `CONDITIONAL_JUMP`
<a id="insn-00bceb28"></a> `00bceb28` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bceb2c"></a> `00bceb2c` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bceb30"></a> `00bceb30` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bceb34"></a> `00bceb34` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bceb38"></a> `00bceb38` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bceb3c"></a> `00bceb3c` | `85 39 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bceb40"></a> `00bceb40` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bceb44"></a> `00bceb44` | `e0 03 00 b4` | cbz x0,0x00bcebc0 | `CONDITIONAL_JUMP`
<a id="insn-00bceb48"></a> `00bceb48` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bceb4c"></a> `00bceb4c` | `49 47 87 52` | mov w9,#0x3a3a | `FALL_THROUGH`
<a id="insn-00bceb50"></a> `00bceb50` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bceb54"></a> `00bceb54` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bceb58"></a> `00bceb58` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bceb5c"></a> `00bceb5c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bceb60"></a> `00bceb60` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bceb64"></a> `00bceb64` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bceb68"></a> `00bceb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bceb6c"></a> `00bceb6c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bceb70"></a> `00bceb70` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bceb74"></a> `00bceb74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceb78"></a> `00bceb78` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bceb7c"></a> `00bceb7c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bceb80"></a> `00bceb80` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bceb84"></a> `00bceb84` | `c1 00 00 54` | b.ne 0x00bceb9c | `CONDITIONAL_JUMP`
<a id="insn-00bceb88"></a> `00bceb88` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bceb8c"></a> `00bceb8c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bceb90"></a> `00bceb90` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bceb94"></a> `00bceb94` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bceb98"></a> `00bceb98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bceb9c"></a> `00bceb9c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bceba0"></a> `00bceba0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bceba4"></a> `00bceba4` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bceba8"></a> `00bceba8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcebac"></a> `00bcebac` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcebb0"></a> `00bcebb0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcebb4"></a> `00bcebb4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcebb8"></a> `00bcebb8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcebbc"></a> `00bcebbc` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcebc0"></a> `00bcebc0` | `80 3d 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceac0`](#insn-00bceac0) 範囲 `[['00bceac0', '00bceaff']]`
  - `CONDITIONAL_JUMP` [`00bceafc`](#insn-00bceafc) → [`00bceb14`](#insn-00bceb14)
  - `FALL_THROUGH` [`00bceafc`](#insn-00bceafc) → [`00bceb00`](#insn-00bceb00)
- ブロック [`00bceb00`](#insn-00bceb00) 範囲 `[['00bceb00', '00bceb13']]`
  - `FALL_THROUGH` [`00bceb10`](#insn-00bceb10) → [`00bceb14`](#insn-00bceb14)
- ブロック [`00bceb14`](#insn-00bceb14) 範囲 `[['00bceb14', '00bceb27']]`
  - `CONDITIONAL_JUMP` [`00bceb24`](#insn-00bceb24) → [`00bceb4c`](#insn-00bceb4c)
  - `FALL_THROUGH` [`00bceb24`](#insn-00bceb24) → [`00bceb28`](#insn-00bceb28)
- ブロック [`00bceb28`](#insn-00bceb28) 範囲 `[['00bceb28', '00bceb47']]`
  - `CONDITIONAL_JUMP` [`00bceb44`](#insn-00bceb44) → [`00bcebc0`](#insn-00bcebc0)
  - `FALL_THROUGH` [`00bceb44`](#insn-00bceb44) → [`00bceb48`](#insn-00bceb48)
- ブロック [`00bceb48`](#insn-00bceb48) 範囲 `[['00bceb48', '00bceb4b']]`
  - `FALL_THROUGH` [`00bceb48`](#insn-00bceb48) → [`00bceb4c`](#insn-00bceb4c)
- ブロック [`00bceb4c`](#insn-00bceb4c) 範囲 `[['00bceb4c', '00bceb87']]`
  - `CONDITIONAL_JUMP` [`00bceb84`](#insn-00bceb84) → [`00bceb9c`](#insn-00bceb9c)
  - `FALL_THROUGH` [`00bceb84`](#insn-00bceb84) → [`00bceb88`](#insn-00bceb88)
- ブロック [`00bceb88`](#insn-00bceb88) 範囲 `[['00bceb88', '00bceb9b']]`
- ブロック [`00bceb9c`](#insn-00bceb9c) 範囲 `[['00bceb9c', '00bcebbf']]`
- ブロック [`00bcebc0`](#insn-00bcebc0) 範囲 `[['00bcebc0', '00bcebc3']]`

## 命令位置別の参照

- [`00bceac4`](#insn-00bceac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceac8`](#insn-00bceac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceacc`](#insn-00bceacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceafc`](#insn-00bceafc) → [`00bceb14`](#insn-00bceb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb24`](#insn-00bceb24) → [`00bceb4c`](#insn-00bceb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb3c`](#insn-00bceb3c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bceb44`](#insn-00bceb44) → [`00bcebc0`](#insn-00bcebc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb84`](#insn-00bceb84) → [`00bceb9c`](#insn-00bceb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb88`](#insn-00bceb88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb8c`](#insn-00bceb8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb90`](#insn-00bceb90) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebac`](#insn-00bcebac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebb0`](#insn-00bcebb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebb4`](#insn-00bcebb4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebc0`](#insn-00bcebc0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bceac4`](#insn-00bceac4)

~~~json
{
  "source": "00bceac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceac8`](#insn-00bceac8)

~~~json
{
  "source": "00bceac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceacc`](#insn-00bceacc)

~~~json
{
  "source": "00bceacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceafc`](#insn-00bceafc)

~~~json
{
  "source": "00bceafc",
  "target": "00bceb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb24`](#insn-00bceb24)

~~~json
{
  "source": "00bceb24",
  "target": "00bceb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb3c`](#insn-00bceb3c)

~~~json
{
  "source": "00bceb3c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceb44`](#insn-00bceb44)

~~~json
{
  "source": "00bceb44",
  "target": "00bcebc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb84`](#insn-00bceb84)

~~~json
{
  "source": "00bceb84",
  "target": "00bceb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb88`](#insn-00bceb88)

~~~json
{
  "source": "00bceb88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb8c`](#insn-00bceb8c)

~~~json
{
  "source": "00bceb8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb90`](#insn-00bceb90)

~~~json
{
  "source": "00bceb90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebac`](#insn-00bcebac)

~~~json
{
  "source": "00bcebac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebb0`](#insn-00bcebb0)

~~~json
{
  "source": "00bcebb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebb4`](#insn-00bcebb4)

~~~json
{
  "source": "00bcebb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebc0`](#insn-00bcebc0)

~~~json
{
  "source": "00bcebc0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
