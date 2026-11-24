# 00bfcd2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b802e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-e786686703e20a7cbed8224750eb45a1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfd154`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd154.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-8c88b2da7694fb5470aacba8fcddbf84)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcd2c",
  "name": "FUN_00bfcd2c",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f36b8900103d39c7187497624146764d93738a24f06805a88e6d7e5553865ca",
  "source_text_sha256": "4f36b8900103d39c7187497624146764d93738a24f06805a88e6d7e5553865ca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcd2c",
        "00bfcdeb"
      ]
    ],
    "bytes_sha256": "6b670c52366af3a0684a4dc337174cfbcca72d37042b25877f165cd78eb857d9",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfcd24](../00bfc/00bfcd24.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00bfcd2c(long *param_1,undefined8 param_2)

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
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b710
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x50))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
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
<a id="insn-00bfcd2c"></a> `00bfcd2c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcd30"></a> `00bfcd30` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcd34"></a> `00bfcd34` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcd38"></a> `00bfcd38` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcd3c"></a> `00bfcd3c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcd40"></a> `00bfcd40` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcd44"></a> `00bfcd44` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfcd48"></a> `00bfcd48` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcd4c"></a> `00bfcd4c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfcd50"></a> `00bfcd50` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfcd54"></a> `00bfcd54` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcd58"></a> `00bfcd58` | `1e 73 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcd5c"></a> `00bfcd5c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfcd60"></a> `00bfcd60` | `a8 03 00 34` | cbz w8,0x00bfcdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bfcd64"></a> `00bfcd64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcd68"></a> `00bfcd68` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcd6c"></a> `00bfcd6c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bfcd70"></a> `00bfcd70` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcd74"></a> `00bfcd74` | `3f 6c 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcd78"></a> `00bfcd78` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcd7c"></a> `00bfcd7c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcd80"></a> `00bfcd80` | `21 88 43 f9` | ldr x1,[x1, #0x710] | `FALL_THROUGH`
<a id="insn-00bfcd84"></a> `00bfcd84` | `3f 6c 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcd88"></a> `00bfcd88` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcd8c"></a> `00bfcd8c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfcd90"></a> `00bfcd90` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcd94"></a> `00bfcd94` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcd98"></a> `00bfcd98` | `28 29 40 f9` | ldr x8,[x9, #0x50] | `FALL_THROUGH`
<a id="insn-00bfcd9c"></a> `00bfcd9c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcda0"></a> `00bfcda0` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcda4"></a> `00bfcda4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfcda8"></a> `00bfcda8` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00bfcdac"></a> `00bfcdac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfcdb0"></a> `00bfcdb0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bfcdb4"></a> `00bfcdb4` | `37 6c 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcdb8"></a> `00bfcdb8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcdbc"></a> `00bfcdbc` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcdc0"></a> `00bfcdc0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcdc4"></a> `00bfcdc4` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcdc8"></a> `00bfcdc8` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcdcc"></a> `00bfcdcc` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfcdd0"></a> `00bfcdd0` | `34 6c 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcdd4"></a> `00bfcdd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcdd8"></a> `00bfcdd8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcddc"></a> `00bfcddc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcde0"></a> `00bfcde0` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfcde4"></a> `00bfcde4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcde8"></a> `00bfcde8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcd2c`](#insn-00bfcd2c) 範囲 `[['00bfcd2c', '00bfcd63']]`
  - `CONDITIONAL_JUMP` [`00bfcd60`](#insn-00bfcd60) → [`00bfcdd4`](#insn-00bfcdd4)
  - `FALL_THROUGH` [`00bfcd60`](#insn-00bfcd60) → [`00bfcd64`](#insn-00bfcd64)
- ブロック [`00bfcd64`](#insn-00bfcd64) 範囲 `[['00bfcd64', '00bfcdd3']]`
  - `FALL_THROUGH` [`00bfcdd0`](#insn-00bfcdd0) → [`00bfcdd4`](#insn-00bfcdd4)
- ブロック [`00bfcdd4`](#insn-00bfcdd4) 範囲 `[['00bfcdd4', '00bfcdeb']]`

## 命令位置別の参照

- [`00bfcd34`](#insn-00bfcd34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd38`](#insn-00bfcd38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd54`](#insn-00bfcd54) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd58`](#insn-00bfcd58) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd5c`](#insn-00bfcd5c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd60`](#insn-00bfcd60) → [`00bfcdd4`](#insn-00bfcdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd74`](#insn-00bfcd74) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfcd80`](#insn-00bfcd80) → `00c9b710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcd80`](#insn-00bfcd80) → `01127778`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcd84`](#insn-00bfcd84) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdb4`](#insn-00bfcdb4) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdc4`](#insn-00bfcdc4) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdd0`](#insn-00bfcdd0) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfcdd8`](#insn-00bfcdd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcddc`](#insn-00bfcddc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcd34`](#insn-00bfcd34)

~~~json
{
  "source": "00bfcd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd38`](#insn-00bfcd38)

~~~json
{
  "source": "00bfcd38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd54`](#insn-00bfcd54)

~~~json
{
  "source": "00bfcd54",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd58`](#insn-00bfcd58)

~~~json
{
  "source": "00bfcd58",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcd5c`](#insn-00bfcd5c)

~~~json
{
  "source": "00bfcd5c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd60`](#insn-00bfcd60)

~~~json
{
  "source": "00bfcd60",
  "target": "00bfcdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcd74`](#insn-00bfcd74)

~~~json
{
  "source": "00bfcd74",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcd80`](#insn-00bfcd80)

~~~json
{
  "source": "00bfcd80",
  "target": "00c9b710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfcd80`](#insn-00bfcd80)

~~~json
{
  "source": "00bfcd80",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfcd84`](#insn-00bfcd84)

~~~json
{
  "source": "00bfcd84",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcdb4`](#insn-00bfcdb4)

~~~json
{
  "source": "00bfcdb4",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcdc4`](#insn-00bfcdc4)

~~~json
{
  "source": "00bfcdc4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcdd0`](#insn-00bfcdd0)

~~~json
{
  "source": "00bfcdd0",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcdd8`](#insn-00bfcdd8)

~~~json
{
  "source": "00bfcdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcddc`](#insn-00bfcddc)

~~~json
{
  "source": "00bfcddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
