module memory_code #(parameter N = 2)
    (input [(2*N) - 1:0] address,
    input read_en,
    input en,
    output [(2*N) - 1:0] data);
                
    reg [(2*N) - 1:0] mem [0: 2**(2*N)-1];
    assign data = (en && read_en) ? mem[address] : 0;
    
    initial begin

    $readmemb("rom_{0}x{1}.dat", mem);
        end
    endmodule